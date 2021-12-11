# AutoWaterPi
An auto machine that water your plant. with auto picture capture function.

# IT'S NOT WORKING NOW!
under developing

# Preconfiguration    

In `init.sh`.  
Variable `minute` determine the interval of water tray level and moisture check. Default is `5`  
Variable `cminute` determine the interval of picture captures. Default is `15`  


# Installation    

Run `init.sh` as root, it will put `check.py` and `capture.py` into crontab.  
By this, it can check Water level on tray and soil moisture periodically.  
Also, it will install apache2 automatically.  
You can watch the pictures captured at `Your IP/AutoWaterPi/Captured` after installation.  


# Configuration
You can still edit the interval of time after installation by command `crontab -u root -e`

### Pin of Miscellaneous
water pump: defined in `water.py`  
Water tray level detector: defined in `check.py`   
Soil moisture detector: defined in `check.py`   

### Editing the pouring value of water each time

### Naming of pictures
Defined in `capture.py`, the `timestamp` variable.

# Removal  
The remove.sh can help you remove the schedules set while installation.
But apache2 won't be remove while uninstallation.
Run it as root.
