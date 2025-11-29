def open_list(Songs):
    with open(Songs,'r', encoding='utf-8') as file:
        Themes= [line.strip() for line in file if line.strip()]
    
    print('Original Songs')
    for single in Themes:
        print(f'Track: {single}')

    Themes.sort()

    with open('ordered_Songs.txt', 'w', encoding='utf-8' ) as list:
        for single in Themes:
            list.write(single+'\n')
            print(f'Ordered:{single}')
            
    
    
    

open_list('ordered_Songs.txt')
open_list('Songs.txt')
