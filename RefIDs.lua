local mod = require "mod.lua"
local newEvent = script.Parent.Parent:WaitForChild("NewEvent")

local appName = "appname1"
local appID = 2
local ZIndex = 5


local TabID = 3
local objID = 3

newEvent.Event:Connect(function(ID, newID)
    if ID == TabID then
        TabID = newID
    end
end)

local remList = mod.remove(3, appName, appID)

for count =1, #remList, 2 do
    newEvent:Fire(remList[count],remList[count+1])
end