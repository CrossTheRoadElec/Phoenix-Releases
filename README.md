# Releases for Phoenix-Framework and Phoenix-Tuner
This is a release repository for users who prefer the GitHub interface over downloading-from-the-site.

This also allows for GitHub users to press "Watch", so that they are made aware when new software is available.

# Phoenix Framework (Installer includes Tuner)  

https://phoenix-documentation.readthedocs.io/en/latest/ch03_PrimerPhoenixSoft.html

# Phoenix Tuner 

![image](https://user-images.githubusercontent.com/14191527/50705437-d16f9d80-1028-11e9-83a9-d9c69bba1a66.png)


### What is this?
This repository  holds binary releases for Phoenix Tuner.  Tuner is the 2019 replacement for the FRC Web-Based Configuration Utility that was provided during the previous years. It currently includes all the features of the Web-Based Config with aspirations to include more.

Note: Phoenix Tuner is also installed in the FRC Kickoff Phoenix Installer.  This repository allows for minor updates without cutting an entirely new Phoenix Installer.

### Release Contents:
 - Binary files under CTRE.Phoenix.Diagnostics/Binary/ that contains the Server Executable and startup scripts to automatically run the server on RoboRIO startup.
 - Phoenix CCI library that is deployed to the FRC roboRIO (matches kickoff release).
 
### How to get it running
1. Run application
2. Connect RoboRIO to pc over USB
3. Select "172.22.11.2:1250" inside the Diagnostic Server Address Bar
4. Press "Install Phoenix Library/Diagnostics" button under Prepare the Target Robot Controller
5. Wait for a connection, and you're good to go

Note: This requires a 2019 formatted roboRIO.

Note: Recommended monitor **resolution is 1920 X 1080**.  Future releases will better support higher resolutions/higher dpi.

### Documentation:
Phoenix Tuner use cases are explained here...
https://phoenix-documentation.readthedocs.io/en/latest/

### How it works:
Tuner installs the Phoenix diganostics server, an HTTP server that the client is able to query and retrieve information from. The client does this with HTTP requests, while the server responds with the specified information.

#### Details on how it works
Every http request is sent with a modified url. The url is based on this template:
`http://<address>:<port>/?device=<model>&id=<id>&action=<action>&<furtherArgs>`
 - address - This is the address of the target the server is on. For a RoboRIO it will be 172.22.11.2 over USB, and 10.TE.AM.x over ethernet/wifi.
 - port - This is the port of the serveras specified in the startup script. This can be changed in the script by the user if they want a different port. By default it is **1250**.
 - model - This is a string literal of the model of the target device. It can be: 
    - srx
    - spx
    - canif
    - pigeon
    - ribbonPigeon
    - pcm
    - pdp
 - id - This is the id of the target device.
 - action - This is the action to do with regards to the target device. It can include:
    - getversion
    - getdevices
    - blink
    - setid (newid=)
    - setname (newname=)
    - selftest
    - fieldupgrade
    - progress
    - getconfig
    - setconfig
 - furtherArgs - These are arguments specific to a certain command. As of the time of this writing this includes only setid and setname, as a new id/name must be specified in the url to set these names to.
