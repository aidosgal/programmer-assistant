import os
import subprocess
from take_command import takeCommand
from assistant import speak



def git_commit():

    folder_path = './'
    commit_message = 'feat: add new feature'

    speak("Enter the path of the folder you want to commit changes to:")

    folder_path2 = takeCommand()

    speak("Enter the commit message:")

    commit_message2 = takeCommand()
    # Change directory to the specified folder
    os.chdir(folder_path)

    # Add all changes to the staging area
    subprocess.run(['git', 'add', '.'])

    # Commit the changes with the given commit message
    subprocess.run(['git', 'commit', '-m', commit_message])\
    
    subprocess.run(['git', 'push', 'origin', 'main'])
git_commit()
