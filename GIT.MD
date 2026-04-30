### WHEN A PROJECT IS NEW
on github.con -create a repository 
a provide the repository name
b set privacy
c get your repio url on creation
 - start git process from project terminal
1, initializing the git folder : git init
2. connect local project to repo url:
git remote add origin
3. initial adding of files : git add.
4 make commit : git commit -m"write a commit msg"
5. ensure you a password token to allow push
6. push using token via this comand git push origin master
where master is referencing the default branch where work will be saved
### incase the push doesnt work based off permissions
-git auth logout
-git auth login
 - require your personal token
after login proceed to do push
## to get project on a new device
- select project saving location - open terminal
- git clone linkto repo
## to update project repo
- git add .
- git commit -m ""
- git push -u origin master/main