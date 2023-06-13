#import glob
import glob
#import os
import os
#import sys
import sys
#import argparse
import argparse
import random
#import time
import time
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

#import carla
import carla
#create a list name actor_list
actor_list= []
def main(arg):
    client= carla.Client('localhost', 2000)
    client.set_timeout(2.0)
    world= client.get_world()


    """Main function of the script"""
    #python script for host and port declaration and put in client variable
    #Time to wait for screen
    #Define get_world() method and save in world variable

    #define try

        #define blueprint of world
        #vehicle model

        #location for the vehicle
    try:
        get_blueprint_of_world= world.get_blueprint_library()
        vehicle_bp= get_blueprint_of_world.filter('model3')[0]
        vehicle_transform= (world.get_map().get_spawn_points()[0])
        vehicle = world.spawn_actor(vehicle_bp, vehicle_transform) #call vehicle with variable name dropped_vehicle
        vehicle.set_autopilot(True) #set vehicle as autopilot

        spectator_transform = carla.Transform(vehicle_transform.location, vehicle_transform.rotation)
        spectator_transform.location += vehicle_transform.get_forward_vector() * 20
        spectator_transform.rotation.yaw += 180
        spectator = world.get_spectator()
        spectator.set_transform(spectator_transform)
        vehicle.set_transform(vehicle_transform)
        actor_list.append(dropped_vehicle)

        #put time in sleep for 1000
        time.sleep(1000)

    finally:
        print('destroying actors')
        for actor in actor_list:
            actor.destroy()
        #create a loop for actor in actor_list
            #actor every actor
        print('done.')


