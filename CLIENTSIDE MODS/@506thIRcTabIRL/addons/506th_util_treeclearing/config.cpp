#include "\506th_util_treeclearing\script_component.hpp"

class CfgPatches
{
	class 506th_util_treeclearing
	{
		author = "506th Mod Team";
		name = "Tree Clearing";
		requiredAddons[] = {"ace_interact_menu", "cba_keybinding", "cba_main", "cba_main_a3", "cba_settings", "extended_eventhandlers"};
		requiredVersion = 2.00;
		units[] = {};
		weapons[] = {};
	};
};

// class CfgFunctions {
// 	class f506th_Melee {
// 		class Melee {
// 			file = "\506th_util_melee\functions";
// 			class weaponMelee {};
// 			class windowBreaker {};
// 			class ragdoll {};
// 		};
// 	};
// };

class Extended_PreStart_EventHandlers {
    class ADDON {
        init = call compile preprocessFileLineNumbers "506th_util_treeclearing\XEH_preStart.sqf";
    };
};