bd_division_info = {}
bd_division_info["Barishal"] = {"district": 6, "upazila": 39, "union": 333}
bd_division_info["Chittagong"] = {"district": 11, "upazila": 97, "union": 336}
bd_division_info["Dhaka"] = {"district": 13, "upazila": 93, "union": 1833}
bd_division_info["Khulna"] = {"district": 10, "upazila": 59, "union": 270}
bd_division_info["Mymensingh"] = {"district": 4, "upazila": 34, "union": 350}
bd_division_info["Rajshahi"] = {"district": 8, "upazila": 70, "union": 558}
bd_division_info["Rangpur"] = {"district": 8, "upazila": 58, "union": 536}
bd_division_info["Sylhet"] = {"district": 4, "upazila": 38, "union": 334}

divisions = bd_division_info.keys()

for division in divisions:
    print('Division', division,'has',bd_division_info[division]['district'], 'districts.')
    print('Division', division,'has',bd_division_info[division]['upazila'], 'Upazila.')

#To see the content of bd_division_info
#Methode 1
for key in bd_division_info:
    print(key, '\n', bd_division_info[key])

print("\n\n---------------------------------------\n\n")
#Methode 2
for key, value in bd_division_info.items():
    print(key)
    print(value)

