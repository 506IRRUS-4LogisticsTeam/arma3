#include "script_component.hpp"

if ( GVAR(key) == "" ) then {
	private _str = (ceil random 1000000) toFixed 0;
	_str = ['000000', _str] joinString ''; 
	private _key = _str select [count _str - 6, 6] ;
	[QGVAR(key), _key, 0, "client", true] call CBA_settings_fnc_set;
};

INFO_1("Connect to %1", "https://ctab.506thir.net/hub");

// Connects to server
"cTabExtension" callExtension ["Connect", ["https://ctab.506thir.net/hub", getPlayerUID player, profileName, GVAR(key)]];

// Send mission data
"cTabExtension" callExtension ["StartMission", [worldName, worldSize, date]];

// Setup initial loadout
call FUNC(updateDevices);