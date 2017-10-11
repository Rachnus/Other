#pragma semicolon 1

#define PLUGIN_AUTHOR "Rachnus"
#define PLUGIN_VERSION "1.0"

#include <sourcemod>
#include <sdktools>
#include <cstrike>
#include <socket>
//#include <sdkhooks>

#pragma newdecls required

EngineVersion g_Game;
Handle g_hSocket;

public Plugin myinfo = 
{
	name = "Raspberry Weapon Fire",
	author = PLUGIN_AUTHOR,
	description = "Will send data to a server when the a weapon is fired",
	version = PLUGIN_VERSION,
	url = "https://github.com/Rachnus"
};

public void OnPluginStart()
{
	g_Game = GetEngineVersion();
	if(g_Game != Engine_CSGO && g_Game != Engine_CSS)
	{
		SetFailState("This plugin is for CSGO/CSS only.");	
	}
	
	HookEvent("weapon_fire", Event_WeaponFire);
	
	Handle socket = SocketCreate(SOCKET_TCP, OnSocketError);
	ConnectSocket(socket);
	g_hSocket = socket;
}

public Action Event_WeaponFire(Event event, const char[] name, bool dontBroadcast)
{
	SocketSend(g_hSocket, "thetinggoesskrrrrrrr");
	PrintToServer("FIRE!");
}

public int OnSocketConnected(Handle socket, any arg) 
{
	//Nothing
}

public int OnSocketReceive(Handle socket, char[] receiveData, const int dataSize, any hFile) 
{
	//Nothing

}

public int OnSocketDisconnected(Handle socket, any arg) 
{
	//Nothing
}

public int OnSocketError(Handle socket, const int errorType, const int errorNum, any arg) 
{
	LogError("Socket Error Type: %d Error Num: %d", errorType, errorNum);
	PrintToServer("[raspberryweaponfire.smx] Socket error (Socket Error Type: %d Error Num: %d)", errorType, errorNum);
}

stock void ConnectSocket(Handle socket)
{
	if(!SocketIsConnected(socket))
	{
		PrintToServer("[raspberryweaponfire.smx] Socket Connected");
		SocketConnect(socket, OnSocketConnected, OnSocketReceive, OnSocketDisconnected, "192.168.1.100", 1738);
	}
}
	