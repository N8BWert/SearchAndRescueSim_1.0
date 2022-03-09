louisiana_population = 4649000
TOTAL_POPULATION = louisiana_population / 2
#https://www.wtsp.com/article/weather/tropics/study-21-of-people-wouldnt-leave-for-a-mandatory-hurricane-evacuation-order/67-b8245e8c-e80b-41bf-95e1-f72779e989e1
# study suggests that 21% of people would stay in a storm area even with mandatory evacuation warning
DISCOVER_PERCENTAGE = 21
# assuming the search and rescue teams move at about 15 miles per hour
# 15 miles per hour * 1609 meters/mile * 1 hour/3600 seconds
MOVE_SPEED = 15 * 1609 / 3600
MAX_PEOPLE_PER_LOCATION = 10
TIME_TO_RESCUE_PERSON = 10 * 60
SAVE_CUTOFF_DISTANCE = MOVE_SPEED
INFORM_DISTANCE_CUTOFF = 10 * 1609
TIME_BETWEEN_SENDS = 6 * 60 * 60
NO_PEOPLE_COOLDOWN = 5 * 60