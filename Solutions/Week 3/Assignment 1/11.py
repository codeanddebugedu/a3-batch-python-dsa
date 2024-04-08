def damage(damage, speed, time):
    if speed < 0 or damage < 0:
        return "invalid"
    if time == "second":
        return damage * speed
    if time == "minute":
        return damage * speed * 60
    if time == "hour":
        return damage * speed * 3600
