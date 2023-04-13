local module = {
    ["appname1"] = {}
    ["appname2"] = {}
    ["appname3"] = {}
    ["appname4"] = {}
}

local TabIDs = {1,2,3,4,5}

local objsList = {obj1,obj2,obj3,obj4,obj5}
local ActiveTabs = {1,2,4,5,3}


function module.Remove(id,appName, appID)
    table.remove(module[appName],appID)

    local newTabIDs = {}
    for count = 1, #TabIDs-1, 1 do
        table.insert(newTabIDs,count)
    end
    local reNewTabs = TabIDs
    table.remove(reNewTabs,table.find(id))
    table.remove(objsList,ID)
    local combList = {}
    for count = 1, #reNewTabs, 1 do
        table.insert(combList,reNewTabs[count])
        table.insert(combList,newTabIDs[count])
    end

    local ActList = {}
    for count = 1, #ActiveTabs-1, 1 do
        table.insert(ActList,count)
    end
    ActiveTabs = ActList

    return combList
end



return module