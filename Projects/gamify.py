def initialize():
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars

    global cur_star, cur_star_activity

    #Code that we added - tired and using star
    global tired 
    tired = False
    
    
    cur_hedons = 0
    cur_health = 0
    cur_time = 0

    
    cur_star = None
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    
    last_finished = -1000
    

    global bored_count, boredTime1, boredTime2
    bored_count = 0
    boredTime1 = 0
    boredTime2 = 0



def print_tired():
    return tired

def star_can_be_taken(activity):
    if cur_time == last_finished and bored_with_stars == False and cur_star_activity == activity:
        return True
    else:
        return False

    
def perform_activity(activity, duration):
    global cur_hedons, cur_health, cur_star, tired, cur_time, last_finished, last_activity_duration, last_activity, cur_star_activity
#A check for if the user is tired by checking the timestamp
    if cur_time - last_finished >= 120:
        tired = False  
    else:
        tired = True
    
#Health points given based on "running"
    if activity == "running":
        #checking if the last activity is the same
        if last_activity == activity:
            if duration + last_activity_duration <= 180:
                cur_health += 3 * (duration)
            else:
                cur_health += 3 * (180 - last_activity_duration) + 1 * (duration + last_activity_duration - 180)
        #if the last activity is not the same
        else:
            #While duration is less than 180, the user earns 3 health points per minute
            if duration <= 180:
                cur_health += 3 * duration
            #After 180 minutes of earning 3 points per minute, the user only gains 1 health point per minnute
            else:
                cur_health += 3 * 180 + 1 * (duration - 180)

        #adding our Hedons to the user in the given activity based on stars used and if they are tired 
        if tired == True and cur_star_activity != activity:
            cur_hedons += (-2) * duration
        
        #Headons given due to the use of a star
        if cur_star_activity == activity and tired == False:
            if duration <= 10:
                cur_hedons += 3 * duration 
            else:
                cur_hedons += 3 * 10

        if tired == True and cur_star_activity == activity:
            if duration <= 10:
                cur_hedons += 3 * duration - 2 * duration
            else:
                cur_hedons += 3 * 10 - 2 * duration

        cur_star == False
        #adding our Hedons to the user in the given activity if they are not tired
        if tired == False and cur_star_activity != activity:
            #While the duration is less than 10 minutes, the user earns 2 hedons per minute
            if duration <= 10:
                cur_hedons += 2 * duration
            #While the duration is more than 10 minutes, the user loses 2 hedons per minute
            else:
                cur_hedons += 20 - 2 * (duration - 10)
        #running timestamps
        last_finished = cur_time + duration
        cur_time += duration
        last_activity_duration = duration
        last_activity = activity
        cur_star_activity = None
        



    
#Health points given based on "carrying textbooks"
    if activity == "textbooks":
        #While the user carries textbooks their health points degrade 2 per minute
        cur_health += 2 * duration
        
        #adding our Hedons to the user in the given activity based on stars used and if they are tired 
        if tired == True and cur_star_activity != "textbooks":
            cur_hedons -= 2 * duration 
        #hedons given if the user carries textbooks for less than 20 minutes
        if tired == False and cur_star_activity != "textbooks": 
            if duration <= 20:
                cur_hedons += 1 * duration
            else:
        #hedons given if the user carries textbooks for more than 20 minutes
                cur_hedons += 20 - 1 * (duration - 20)
        
        #Headons given due to the use of a star and accounting for if they are tired
        if cur_star_activity == activity and tired == False:
            if duration <= 10:
                cur_hedons += 3 * duration
            else:
                cur_hedons += 3 * 10

        
        if cur_star_activity == activity and tired == True:
            if duration <= 10:
                cur_hedons += 3 * duration - 2 * duration
            else:
                cur_hedons += 3 * 10 - 2 * duration

        cur_star == False
        #textbooks timestamps
        last_finished = cur_time + duration
        cur_time += duration
        last_activity_duration = duration
        last_activity = activity
        cur_star_activity = None
        
        
    
#Health points given based on "resting"  
    if activity == "resting":
        #While the user is resting, the user does not gains 0 hedons per minute
        cur_health += 0 * duration
        #resting timestamps
        cur_time += duration
        last_activity_duration = duration
        last_activity = activity
        cur_star_activity = None 

def get_cur_hedons():
    #return the current hedons
    return cur_hedons
    
def get_cur_health():
    #return the current health
    return cur_health 


def offer_star(activity):
    global cur_star_activity
    global bored_count, boredTime1, boredTime2, bored_with_stars

    if bored_count == 3:
        cur_star_activity = None
        pass
    
    if bored_count == 2:
        if cur_time - boredTime1 > 120:
            boredTime1 = cur_time
            bored_count = 1
            pass
        else:
            bored_with_stars = True
            bored_count += 1
            cur_star_activity = None
            pass
    
    if bored_count == 1:
        if cur_time - boredTime1 > 120:
            boredTime1 = cur_time
            cur_star_activity = activity
            pass
        else:
            bored_count += 1
            cur_star_activity = activity
            pass
            
    if bored_count == 0:
        boredTime1 = cur_time
        bored_count += 1
        cur_star_activity = activity
        pass
        
def most_fun_activity_minute():
    global cur_hedons, cur_health, cur_star, tired, cur_time, last_finished, last_activity_duration, last_activity, cur_star_activity

    temp_cur_hedons = cur_hedons
    temp_health = cur_health
    temp_star = cur_star
    temp_tired = tired
    temp_time = cur_time
    temp_last_finished = last_finished
    temp_last_activity_duration = last_activity_duration
    temp_last_activity = last_activity
    temp_cur_star_activity = cur_star_activity

    #hedons for 1 minute of running
    hedonsI = get_cur_hedons()
    perform_activity("running", 1)
    hedonsRunning = get_cur_hedons() - hedonsI

    cur_hedons = temp_cur_hedons
    cur_health = temp_health
    cur_star = temp_star
    tired = temp_tired
    cur_time = temp_time
    last_finished = temp_last_finished
    last_activity_duration = temp_last_activity_duration
    last_activity = temp_last_activity
    cur_star_activity = temp_cur_star_activity 


    #hedons for 1 minute of textbooks
    hedonsI = get_cur_hedons()
    perform_activity("textbooks", 1)
    hedonsTextbooks = get_cur_hedons() - hedonsI

    cur_hedons = temp_cur_hedons
    cur_health = temp_health
    cur_star = temp_star
    tired = temp_tired
    cur_time = temp_time
    last_finished = temp_last_finished
    last_activity_duration = temp_last_activity_duration
    last_activity = temp_last_activity
    cur_star_activity = temp_cur_star_activity 
    
    #hedons for 1 minute of resting
    hedonsI = get_cur_hedons()
    perform_activity("resting", 1)
    hedonsResting = get_cur_hedons() - hedonsI

    cur_hedons = temp_cur_hedons
    cur_health = temp_health
    cur_star = temp_star
    tired = temp_tired
    cur_time = temp_time
    last_finished = temp_last_finished
    last_activity_duration = temp_last_activity_duration
    last_activity = temp_last_activity
    cur_star_activity = temp_cur_star_activity 


    #reset all values to before
    cur_hedons = temp_cur_hedons
    cur_health = temp_health
    cur_star = temp_star
    tired = temp_tired
    cur_time = temp_time
    last_finished = temp_last_finished
    last_activity_duration = temp_last_activity_duration
    last_activity = temp_last_activity
    cur_star_activity = temp_cur_star_activity 

    if hedonsRunning > hedonsTextbooks and hedonsRunning > hedonsResting:
        return "running"
    if hedonsTextbooks > hedonsRunning and hedonsTextbooks > hedonsResting:
        return "textbooks"
    if hedonsResting > hedonsTextbooks and hedonsResting > hedonsRunning:
        return "resting"   

################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("resting", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("running")
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    offer_star("running")
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    perform_activity("resting", 30)
    print(get_cur_health())
    print(get_cur_hedons())    
    






