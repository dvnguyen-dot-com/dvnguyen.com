---
draft: True
revision: 1
template: base.html
title: My Setup for Juggling between Projects
tags: ["setup"]
---

At work we use a single monolith Git repository for our entire code base. Even I'm not a big fan of multi-tasking, I often find myself juggling between branches for features, bugfixes, or code review. For example, when one of my PR is up and waiting for code review, I pull up a teammate PR to review it. Or sometimes when a task running over a large amount of data, I switch to another task to not wasting time. Switch branch means losing current editor state, which leads to higher context switch cost and harder to get back to the zone. Sometimes it's even impossible if I have a running script. To solve this problem, I use `git worktree` to make a separate folder for each branch, and `tmux` for managing sessions. My editor of choice is `neovim`, so it's easier to seamlessly integrate with `git worktree` and `tmux`.

To make new worktree: usually from my "master" worktree:
`git worktree add -b <branch_name> ../repo-name-worktree-name`

For example:
`git worktree add -b feature/dave/HVST-12345/cool-feature ../hvst-cool-feature`, where `HVST-12345` is the Jira ID for the feature.

Make new tmux session for the worktree:
```
cd path/to/hvst-cool-feature
tmux new -s cool-feature
```

To preserve tmux sessions between computer reboots, I use TODO

To switch between worktree, just switch between tmux sessions: `CLTR+B s`

I put a `.editorconfig` file in the parent folder of my work code base.

This is the link to my dotfile: TODO

Pros and Cons
Pros:
- This setup can be applied for juggling between multiple projects, not just worktrees of a single projects
- If you use the terminal for everything, all the things you need for a task are kept. When you switch back to an old task, all you need to resume working are already there.

Cons:
- If you don't use terminal for development, it's hard to integrate with worktree. For example, if you create new worktree for each branch, Intellij IDEs would need to re-index everytime you switch the folder, which could be unbearable.
