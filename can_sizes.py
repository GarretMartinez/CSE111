import math

def main():

    can1 = '1 Picnic'
    vol = cylinder_volume(6.83, 10.16)
    sa = cylinder_surface_area(6.83, 10.16)
    eff = storage_efficiency(vol, sa)
    print(f'{can1}, {eff:.1f}')

    can2 = '1 Tall'
    vol = cylinder_volume(7.78, 11.91)
    sa = cylinder_surface_area(7.78, 11.91)
    eff = storage_efficiency(vol, sa)
    print(f'{can2}, {eff:.1f}')

    can3 = '2'
    vol = cylinder_volume(8.73, 11.59)
    sa = cylinder_surface_area(8.73, 11.59)
    eff = storage_efficiency(vol, sa)
    print(f'{can3}, {eff:.1f}')

    can4 = '2.5'
    vol = cylinder_volume(10.32, 11.91)
    sa = cylinder_surface_area(10.32, 11.91)
    eff = storage_efficiency(vol, sa)
    print(f'{can4}, {eff:.1f}')

    can5 = '3 Cylinder'
    vol = cylinder_volume(10.79, 17.78)
    sa = cylinder_surface_area(10.79, 17.78)
    eff = storage_efficiency(vol, sa)
    print(f'{can5}, {eff:.1f}')

    can6 = '5'
    vol = cylinder_volume(13.02, 14.29)
    sa = cylinder_surface_area(13.02, 14.29)
    eff = storage_efficiency(vol, sa)
    print(f'{can6}, {eff:.1f}')

    can7 = '6Z'
    vol = cylinder_volume(5.40, 8.89)
    sa = cylinder_surface_area(5.40, 8.89)
    eff = storage_efficiency(vol, sa)
    print(f'{can7}, {eff:.1f}')

    can8 = '8Z short'
    vol = cylinder_volume(6.83, 7.62)
    sa = cylinder_surface_area(6.83, 7.62)
    eff = storage_efficiency(vol, sa)
    print(f'{can8}, {eff:.1f}')

    can9 = '10'
    vol = cylinder_volume(15.72, 17.78)
    sa = cylinder_surface_area(15.72, 17.78)
    eff = storage_efficiency(vol, sa)
    print(f'{can9}, {eff:.1f}')

    can10 = '211'
    vol = cylinder_volume(6.83, 12.38)
    sa = cylinder_surface_area(6.83, 12.38)
    eff = storage_efficiency(vol, sa)
    print(f'{can10}, {eff:.1f}')

    can11 = '300'
    vol = cylinder_volume(7.62, 11.27)
    sa = cylinder_surface_area(7.62, 11.27)
    eff = storage_efficiency(vol, sa)
    print(f'{can11}, {eff:.1f}')

    can12 = '303'
    vol = cylinder_volume(8.10, 11.11)
    sa = cylinder_surface_area(8.10, 11.11)
    eff = storage_efficiency(vol, sa)
    print(f'{can12}, {eff:.1f}')

def cylinder_volume(radius, height):    
    vol = math.pi * radius ** 2 * height
    return vol

def cylinder_surface_area(radius, height):
    sur_area = 2 * math.pi * radius * (radius + height)
    return sur_area
 
def storage_efficiency(vol, sa):
    efficiency = vol / sa
    return efficiency


main()