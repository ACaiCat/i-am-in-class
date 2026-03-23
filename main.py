from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from gql.transport.exceptions import TransportQueryError

from app.api import *
from app.client import get_client
from app.config import settings
from app.models import LocationInfo


def main():
    client = get_client()

    tongjis = get_all_baoming_records(client, GetAllBaomingRecordsVariables(
        uid=settings.user_id,
        limit="20",
    ))

    for record in tongjis.baomings:
        result = get_tongji(client, GetTongjiVariables(
            _id=record.tongjiId,
        ))
        if result.tongji.allowSubmitTimeRules and result.tongji.allowSubmitTimeRules[0]:
            time_str = result.tongji.allowSubmitTimeRules[0].endTime.split()[0]
            end_time = datetime.strptime(time_str, "%H:%M").time()
            diff: timedelta = datetime.combine(datetime.today(), end_time) - datetime.now()
            if timedelta(0) < diff < timedelta(minutes=10) or settings.sign_any_time:
                try:
                    create_baoming(client, CreateBaomingVariables(
                        userId=settings.user_id,
                        tongjiId=result.tongji.id_,
                        infoKey=["姓名"],
                        infoVal=[settings.name],
                        signUrl="",
                        locationInfo=LocationInfo(
                            name=settings.location_name,
                            longtitude=settings.location_lon,
                            lattitude=settings.location_lat
                        ),
                        no=int(settings.school_no),
                        noLabel=settings.school_no
                    ))
                    print(f"【{result.tongji.title}】打卡成功!")
                except TransportQueryError as e:
                    if e.errors[0].startswith("重复请求"):
                        print(f"【{result.tongji.title}】已存在打卡记录!")
                    else:
                        print(f"【{result.tongji.title}】{e.errors[0]}!")
                except Exception as e:
                    print(f"【{result.tongji.title}】打卡失败! {str(e)}")


if __name__ == "__main__":
    main()
    print(f"调度启动，cron表达式：{settings.cron}")
    scheduler = BlockingScheduler()
    scheduler.add_job(main, CronTrigger.from_crontab(settings.cron))
    scheduler.start()
