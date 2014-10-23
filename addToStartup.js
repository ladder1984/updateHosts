function CreateShortcut(target_path)
{
   wsh = new ActiveXObject('WScript.Shell');
   link = wsh.CreateShortcut(wsh.SpecialFolders("Startup") + '\\updateHosts.lnk');
   link.TargetPath = '"' + wsh.CurrentDirectory + '\\updateHosts.py"';
   link.Arguments = '"' + wsh.CurrentDirectory + '\\updateHosts.py"';
   link.WindowStyle = 7;
   link.Description = 'updateHosts';
   link.WorkingDirectory = wsh.CurrentDirectory;
   link.Save();
}

function main()
{
    CreateShortcut();
}

main();
