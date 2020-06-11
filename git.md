

## 一、创建、提交、修改

### 创建本地仓库

使用 `git init` 后，会创建一个 `.git` 隐藏文件夹，这个文件夹是我们的版本库

~~~
mkdir newFolder
cd newFolder
git init
~~~

查看路径：

~~~
pwd
~~~

### 添加，提交

~~~
git add <file/folder>
git commit -m "add a new file"
~~~

添加多个文件：

~~~
git add f1.txt f2.txt
git commit -m "add two files."
~~~

### 查看当前状态，是否被修改：

~~~
git status
~~~

### 对比文件，查看修改的地方：

~~~
git diff xx.txt
~~~

## 二、版本回退

### 查看提交的历史记录：

~~~
git log
~~~

### 回到上一个版本

HEAD表示当前版本，HEAD^ 表示上一个版本，HEAD^^ 表示上上个版本，HEAD~100 表示上100个版本。

~~~
git reset --hard HEAD^
~~~

### 查看历史记录

通过git log查看历史记录，使用 commit 号回退：只需要写前几位就行了

~~~
git log
git reset --hard 1094a
~~~

通过reset命令回退到某一版本后，无法查看之前的最新的版本了(未来的版本），可以使用这个查看：

~~~
git reflog
~~~

### 工作区和暂存区

你的git仓库正常的文件夹，就是你的工作区。在git仓库中，当你 `git init` 后，会自动生成一个`.git`的隐藏文件夹，它是 git 的版本库，库里面有一个叫 `stage` 的暂存区，还有Git为我们自动创建的第一个分支`master`，以及指向`master`的一个指针叫 `HEAD`, 第一步是用`git add`把文件添加进去，实际上就是把文件修改添加到暂存区；第二步是用`git commit`提交更改，实际上就是把暂存区的所有内容提交到当前分支。

### 撤销修改的方法

1.撤销工作区的修改，尚未使用`add`方法。即只在工作区修改，但是尚未提交到暂存区的修改。（如果你使用了add 提交到了暂存区，它只能让你回到暂存区的状态；没有使用add方法，可以让你回到版本库的状态，也就是撤销所有工作区的修改）

~~~
git checkout -- xx.txt
~~~

2.撤销暂存区的修改，并放回到工作区：使用了`add`方法，提交到了暂存区，但是没有使用`commit`方法提交到当前分支。

~~~
git reset HEAD <file>        # 先撤销暂存区的修改，放回到工作区
git checkout -- xx.txt       # 再撤销工作区
~~~

### 删除文件

~~~
git rm xx.txt
git commit -m "delete xx.txt"
~~~

### 还原删除的文件

~~~
git checkout -- test.txt
~~~

## 三、分支管理

### 创建分支并切换

第一种

~~~
git checkout -b dev
~~~

第二种(新版)

~~~
git switch -c dev
~~~

`git checkout` 加上 `-b` 代表创建分支，并切换到当前分支，等同于下面的命令：

~~~
git branch dev      # 创建分支
git checkout dev    # 切换分支

git switch dev   # 另一种切换分支的方法
~~~

### 查看当前分支

~~~
git branch
~~~

### 合并分支：

将dev分支，合并到当前分支上

~~~
git merge dev
~~~

通常，合并分支时，如果可能，Git会用`Fast forward`模式，但这种模式下，删除分支后，会丢掉分支信息。

如果要强制禁用`Fast forward`模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。

~~~
git merge --no-ff -m "merge with no-ff" dev
~~~

### 删除分支

~~~
git branch -d dev   # 如果没有合并分支，可能删除不掉
git branch -D dev  # 强制删除
~~~

### 合并冲突

当两个分支有冲突时，无法自动完成合并，可以手动查看文件，然后修改，完成合并。

git使用<<<<<<<, ======, >>>>>>> 来标记不同分支的内容。

~~~
$ cat a.txt
I love my mlllllllla
<<<<<<< HEAD
=======

aaaaaaaaaaaaaaaaaaa
>>>>>>> f1

~~~

查看合并记录：

~~~
git log --graph
~~~

### Bug 分支

假设你当前分支的工作做到一半，还不能提交，但是又需要切换到其他分支，修复bug，那可以用 `stash` 将现场存起来，然后切换到其他分支开始临时的工作。

~~~
git stash
~~~

查看stash

~~~
git stash lit
~~~

恢复stash，并手动删除

~~~
git stash apply
git stash drop
~~~

恢复stash并自动删除

~~~
git stash pop
~~~

恢复特定的stash

需要先用`git stash list` 查看

~~~
git stash apply stash@{0}
~~~

同步分支

你用 master 创建了一个分支 bug0，在 bug0 上把 bug 修复了，然后把 bug0  和 master 合并了，这时 master 是修好的，但是 master 的另一个分支 dev 还没有修复好，那怎么能将 dev 上的 bug 也修好？

bug0分支提交修改时：会有一个commit id ：5051635

~~~
/Desktop/github (bug0)
$ git commit -m 'bug fixed'
[bug0 5051635] bug fixed
 Committer: Wang <zhongtao.wang@local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)

~~~

然后切换到 dev 分支，使用命令让我们复制一个特定的提交到当前分支：

~~~
git cherry-pick <commit>
~~~

比如：

~~~
/Desktop/github (dev)
$ git cherry-pick 5051635
[dev 424b6ee] bug fixed
 Date: Tue Jun 9 17:40:56 2020 +0800
 Committer: Wang <zhongtao.wang@cnt01.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)

~~~

这时 dev 的bug也修好了。



## 四、远程仓库

### 添加远程仓库

根据 github 的提示，添加 github 远程仓库

~~~
git remote add origin git@github.com:michaelliao/learngit.git
~~~

推送到远程仓库

第一次推送，带上`-u`参数，会将本地的分支推送到远程，并且和远程的分支关联起来

~~~
git push -u <remote> <local>  # 第一次推送，-u
git push <remote> <local>    # 以后的简化操作
~~~

查看远程仓库信息

~~~
git remote
~~~
查看更详细内容
~~~
git remote -v
~~~
### 克隆远程仓库

默认克隆master

~~~
git clone git@github.com:michaelliao/gitskills.git
~~~

克隆分支

~~~
git checkout -b dev origin/dev  # 创建并克隆远程的dev分支到本地
~~~
设置 dev 分支和远程 origin/dev 分支连接，才能git pull下来
~~~
git branch --set-upstream-to=origin/dev dev  
~~~

多人协作：

1. 首先，可以试图用`git push origin `推送自己的修改；
2. 如果推送失败，则因为远程分支比你的本地更新，需要先用`git pull`试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者解决掉冲突后，再用`git push origin `推送就能成功！

如果`git pull`提示`no tracking information`，则说明本地分支和远程分支的链接关系没有创建，用命令`git branch --set-upstream-to  origin/<branch-name>`。

### rebase(http://gitbook.liuhui998.com/4_2.html)

假设你基于远程仓库 `origin` 创建一个新的分支 `mywork`, 然后你做了几次修改，但是与此同时 `origin` 也被人修改了，这时你想要合并这两条线。

如果正常合并 `merge` ， 会产生一条合并记录（分叉再汇合），如果使用rebase

~~~
$ git checkout mywork
$ git rebase origin
~~~

这些命令会把你的"mywork"分支里的每个提交(commit)取消掉，并且把它们临时 保存为补丁(patch)(这些补丁放到".git/rebase"目录中),然后把"mywork"分支更新 到最新的"origin"分支，最后把保存的这些补丁应用到"mywork"分支上。

这样虽然你的分支线断掉了（插入了origin的更新），但是变成了一条线，没有分叉。

在rebase的过程中，也许会出现冲突(conflict). 在这种情况，Git会停止rebase并会让你去解决 冲突；在解决完冲突后，用"git-add"命令去更新这些内容的索引(index), 然后，你无需执行 git-commit,只要执行:

```
$ git rebase --continue
```

这样git会继续应用(apply)余下的补丁。

在任何时候，你可以用`--abort`参数来终止rebase的行动，并且"mywork" 分支会回到rebase开始前的状态。

```
$ git rebase --abort
```

## 五、标签管理

发布一个版本时，我们通常先在版本库中打一个标签（tag），这样，就唯一确定了打标签时刻的版本。将来无论什么时候，取某个标签的版本，就是把那个打标签的时刻的历史版本取出来。所以，标签也是版本库的一个快照。

标签总是和某个commit挂钩。如果这个commit既出现在master分支，又出现在dev分支，那么在这两个分支上都可以看到这个标签。

创建标签

~~~
git checkout <branch>  # 切换到分支
git tag v1.0          # 打标签
~~~

创建带有说明的标签，用`-a`指定标签名，`-m`指定说明文字

~~~
git tag -a v0.1 -m "version 0.1 released" 1094adb
~~~

列出标签

~~~
git tag
~~~

查看标签信息

~~~
git show <tag name>
~~~

通过commit id 打标签

~~~
git tag v0.9 f52c633
~~~

删除标签

~~~
git tag -d v0.1
~~~

标签推送到远程

~~~
git push origin v1.0
~~~

批量推送标签

~~~
git push origin --tags
~~~

删除远程标签

~~~
git tag -d v0.9         # 先删除本地
git push origin :refs/tags/v0.9
~~~



## Windows配置github

1. 注册github

2. 安装git到本机

3. 配置用户名和邮箱：

   1. `–global` 参数，表示你这台机器上所有的Git仓库都会使用这个配置

   2.  ```
      git config --global user.name “Your Name”
      git config --global user.email "email@example.com"
      ```

4. 创建SSH key，直接三次回车

   1.  ```
      ssh-keygen -t rsa -C "your_email@youremail.com"
      ```


5. 进入.ssh文件夹，里面有两个key, 其中 `id_rsa.pub` 是公钥，打开它，复制里面的内容，在github的设置里面，找到 SSH and GPG keys，添加就ok了

   1.  ```
         
      $ cd ~/.ssh
      $ ls
      id_rsa  id_rsa.pub  known_hosts
      ```

6. 测试是否连上

   1.  ```
      $ ssh -T git@github.com
      Warning: Permanently added the RSA host key for IP address '13.250.177.223' to the list of known hosts.
      Hi wztshine! You've successfully authenticated, but GitHub does not provide shell access.
      
      ```





## others

重命名

~~~
git mv name1 name2
~~~

