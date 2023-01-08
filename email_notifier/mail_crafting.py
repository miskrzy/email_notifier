from datetime import date, timedelta
from typing import List

from email_notifier.garbage_scrapper import GarbageScrapper
from email_notifier.notifications import NotificationGarbage
from email_notifier.email_logging import EmailLogger


def craft_garbage_mails(notifications: List[NotificationGarbage], garbage_scrapper: GarbageScrapper, logger: EmailLogger) -> List[NotificationGarbage]:
    logger.info("Starting of garbage email crafting")
    notifications_garbage_scrapper_inputs = {notific: (notific.get_street(), notific.get_number()) for notific in notifications}
    try:
        garbage_scrapper.set_streets_numbers(list(notifications_garbage_scrapper_inputs.values()))
        waste_schedules = garbage_scrapper.retrieve_streets().retrieve_numbers().get_waste_schedules()
        logger.debug(f"Waste schedules successfully retrieved: {waste_schedules}")
    except Exception as e:
        logger.error(f"Error encountered while using garbage scrappping: {e}")
        raise e
    logger.info("Retrieved waste schedules")

    tomorrow = date.today() + timedelta(days=1)
    after_tomorrow = date.today() + timedelta(days=2)

    content_filled_notifications = []
    for notification, input in notifications_garbage_scrapper_inputs.items():
        tomorrow_schedule = waste_schedules[input].get(tomorrow)
        after_tomorrow_schedule = waste_schedules[input].get(after_tomorrow)
        msg_content = ""
        if tomorrow_schedule:
            logger.info(f"Schedule for tomorrow found for {input}: {tomorrow_schedule}")
            msg_content += f"Typy śmieci wyrzucane jutro ({tomorrow}):\n" + " ".join(tomorrow_schedule) + "\n"
        if after_tomorrow_schedule:
            logger.info(f"Schedule for after tomorrow found for {input}: {after_tomorrow_schedule}")
            msg_content += f"Typy śmieci wyrzucane pojutrze ({after_tomorrow}):\n" + " ".join(after_tomorrow_schedule) + "\n"
        if not tomorrow_schedule and not after_tomorrow_schedule:
            logger.info(f"Did not find any schedules for tomorrow or after tomorrow for {input}")
            continue
        notification.set_content(msg_content)
        content_filled_notifications.append(notification)
    return content_filled_notifications
    