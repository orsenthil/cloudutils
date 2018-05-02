from aws import session
from common import datetimeutils


def delete_all_buckets_older_than_2_days():
    s3 = session.get_s3_session()
    _now = datetimeutils.time_now_at_utc()

    for bucket in s3.buckets.all():
        age = _now - bucket.creation_date
        if age.days > 2:

            try:
                for key in bucket.objects.all():
                    key.delete()

                bucket.delete()
                print("Deleted name: {name}, age: {age}".format(name=bucket.name, age=age))

            except Exception as e:
                print("Failed Deleting {name}".format(name=bucket.name))
