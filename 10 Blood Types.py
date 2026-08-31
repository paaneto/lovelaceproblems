def survive(blood_type, donated_blood):
    
    #blood type = [receives from]
    #M = minus; P = plus

    OM = ["O-"]
    OP = ["O-", "O+"]
    AM = ["A-", "O-"]
    AP = ["A-", "A+", "O-", "O+"]
    BM = ["B-", "O-"]
    BP = ["B-", "B+", "O-", "O+"]
    ABM = ["A-", "B-", "AB-", "O-"]
    ABP = ["A-", "A+", "B-", "B+", "AB-", "AB+", "O-", "O+"]

    if blood_type == "O-":
        if any(item in donated_blood for item in OM):
            return True
        
    if blood_type == "O+":
        if any(item in donated_blood for item in OP):
            return True
    
    if blood_type == "A-":
        if any(item in donated_blood for item in AM):
            return True
        
    if blood_type == "A+":
        if any(item in donated_blood for item in AP):
            return True
        
    if blood_type == "B-":
        if any(item in donated_blood for item in BM):
            return True
        
    if blood_type == "B+":
        if any(item in donated_blood for item in BP):
            return True
        
    if blood_type == "AB-":
        if any(item in donated_blood for item in ABM):
            return True

    if blood_type == "AB+":
        if any(item in donated_blood for item in ABP):
            return True

    return False

survive("B+", ["A-", "B+", "AB+", "O+", "B+", "B-"])

#maybe I should use a dictionary like if value(donated blood) in key(blood type) return true else return false