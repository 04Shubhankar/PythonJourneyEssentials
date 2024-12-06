from datetime import datetime, timezone

# Get the current time in UTC
now = datetime.now(timezone.utc)

# Format the time using formisoformat()
iso_format_time = now.time().isoformat()
print("ISO format time:", iso_format_time)

# Format the time using strftime()
formatted_time = now.time().strftime("%H:%M:%S")
print("Formatted time:", formatted_time)

# Replace the minute and second components of the time
new_time = now.time().replace(minute=30, second=0)
print("New time:", new_time)

# Get the daylight saving time offset (if applicable)
dst_offset = now.timetz().dst()
print("DST offset:", dst_offset)

# Get the time zone name
tz_name = now.timetz().tzname()
print("Time zone name:", tz_name)

# Get the UTC offset
utc_offset = now.timetz().utcoffset()
print("UTC offset:", utc_offset)
