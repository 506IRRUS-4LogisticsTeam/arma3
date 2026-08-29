params ["_interactionType"];

// //Ignore if not enabled:
// if (!GVAR(addBuildingActions)) exitWith {};
//Ignore self-interaction menu:
if (_interactionType != 0) exitWith {};
//Ignore when mounted:
if ((vehicle ACE_player) != ACE_player) exitWith {};

[{
    params ["_args", "_pfID"];
    _args params ["_setPosition", "_addedHelpers", "_housesScaned", "_treesToScanForActions"];

    if (!EGVAR(interact_menu,keyDown)) then {
        {deleteVehicle _x;} forEach _addedHelpers;
        [_pfID] call CBA_fnc_removePerFrameHandler;
        systemChat format ["Looking for Tree"];
    } else {
        // Prevent Rare Error when ending mission with interact key down:
        if (isNull ace_player) exitWith {};

        //Make the common case fast (cursorTarget is looking at a door):
        if (nearestTerrainObjects [ace_player, ["Tree"], 10] > 0) then { //check if unit has explosives
            _treesToScanForActions = [((nearestTerrainObjects [ace_player, ["Tree"], 10] > 0) select 0)];
        };

        //For performance, we only do 1 thing per frame,
        //-either do a wide scan and search for houses with actions
        //-or scan one house at a time and add the actions for that house

        if (_treesToScanForActions isEqualTo []) then {
            //If player moved >2 meters from last pos, then rescan
            if (((getPosASL ace_player) distance _setPosition) < 2) exitWith {};

            // private _nearBuidlings = nearestObjects [ace_player, ["Tree"], 30];
            // {
            //     private _typeOfHouse = typeOf _x;
            //     if (((count (configFile >> "CfgVehicles" >> _typeOfHouse >> "UserActions")) == 0) && {(count (getArray (configFile >> "CfgVehicles" >> _typeOfHouse >> "ladders"))) == 0}) then {
            //         _housesScaned pushBack _x;
            //     } else {
            //         _treesToScanForActions pushBack _x;
            //     };
            //     nil
            // } count (_nearBuidlings - _housesScaned);

            _args set [0, (getPosASL ace_player)];
        } else {
            _treesBeingScaned = _treesToScanForActions deleteAt 0;
            // private _typeOfHouse = typeOf _treesBeingScaned;
            //Skip this house for now if we are outside of it's radius
            //(we have to scan far out for the big houses, but we don't want to waste time adding actions on every little shack)
            if ({((ACE_player distance _treesBeingScaned) > 10}) exitWith {};

            _housesScaned pushBack _treesBeingScaned;

            // private _actionSet = [_typeOfHouse] call FUNC(userActions_getHouseActions);
            // _actionSet params ["_memPoints", "_memPointsActions"];

            // systemChat format ["Add Actions for [%1] (count %2) @ %3", _typeOfHouse, (count _memPoints), diag_tickTime];
            // {
                private _helperPos = [(getPosATL _treesBeingScaned) select 0, (getPosATL _treesBeingScaned) select 1, 0.5];
                					//AGLtoASL (_treesBeingScaned modelToWorld (_treesBeingScaned selectionPosition _x));
                private _helperObject = "ACE_LogicDummy" createVehicleLocal [0,0,0];
                _addedHelpers pushBack _helperObject;
                _helperObject setVariable [QGVAR(building), _treesBeingScaned];
                _helperObject setPosASL _helperPos;
                TRACE_3("Making New Helper",_helperObject,_x,_treesBeingScaned);

                [_helperObject, 0, [], _x] call EFUNC(interact_menu,addActionToObject);

            // } forEach _memPoints;
        };
    };
}, 0, [((getPosASL ace_player) vectorAdd [-100,0,0]), [], [], []]] call CBA_fnc_addPerFrameHandler;