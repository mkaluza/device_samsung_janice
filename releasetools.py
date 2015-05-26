def FullOTA_InstallEnd(info):
	info.script.SetPermissionRecursive("/system/UKM", 0, 0, 0755, 0755, None, None)
	info.script.MakeSymlinks((("/data/UMK/uci", "/system/xbin/uci"), ("/system/UMK/UMK","/system/etc/init.d/99UMK")))
