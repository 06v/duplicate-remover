import sys, os

os.system("cls")

print("""                                                                
 ____              _ _           _         ____                                    
|  _ \ _   _ _ __ | (_) ___ __ _| |_ ___  |  _ \ ___ _ __ ___   _____   _____ _ __ 
| | | | | | | '_ \| | |/ __/ _` | __/ _ \ | |_) / _ \ '_ ` _ \ / _ \ \ / / _ \ '__|
| |_| | |_| | |_) | | | (_| (_| | ||  __/ |  _ <  __/ | | | | | (_) \ V /  __/ |   
|____/ \__,_| .__/|_|_|\___\__,_|\__\___| |_| \_\___|_| |_| |_|\___/ \_/ \___|_|   
            |_|                                                                    """)

count = 0
set1 = set()

file1 = input("\nPath of your Text File which is containing duplicated words:\n")
file2 = input("\nPath of the new Text File which will contain no duplicates:\n")

print("\nLooking for Duplicates!")

try:
	with open (file1, 'r') as file1, open (file2, 'w') as file2:
		for line in file1:
			count += 1
			set1.add(line)
		for line in set1: file2.write(line)
except:
	print("Error! This Program can not access one of your provided Text Files.")

exit(f"\nLocated a total of {count} Lines. After removing duplicated words you are left with {len(set1)} lines!\n\n")
