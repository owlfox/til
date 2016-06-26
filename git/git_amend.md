# git --amend

## amend commit time

It's useful when we faultly commit some thing we don't want to commit.
see the example bellow:
```sh
//1. amend the commit time, useful to make a github streak lol.
git commit --amend --date="Wed May 18 14:00 2016 +0800"
```
the [stackoverflow source is here](http://stackoverflow.com/questions/454734/how-can-one-change-the-timestamp-of-an-old-commit-in-git)

## amend commit user
This can modify user name once you used a wrong user name to commit.
```sh
git commit --amend --author="tjctw <tsejen.tw@gmail.com>"
```
the [stackoverflow source is here](http://stackoverflow.com/questions/3042437/change-commit-author-at-one-specific-commit)
