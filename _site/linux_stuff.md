
# In Linux we trust
Some linux related commands I use from time to time...

## Users & groups
### Create a new user
**useradd** command
```bash
useradd username
```
By default this creates ``/home/username``. 

### Set / change password
**passwd** command
```bash
passwd username
```
 

### Create new group
**groupadd** command
```bash
groupadd <mynewgroup>
```

### Add user to group
**usermod** command
```bash
usermod -a -G <groupname> <username>
```
:::{note}
Uppercase -G assigns new secondary group

Lowercase -g primary group is assigned
:::

### Change / set primary group
A user can be part of several groups, but one of the groups is always the primary, and the others secondary.
```bash
usermod -g <groupname> <username>
```

### What group does a user have access to:
Run the **groups** command
```bash
groups <username>
```
or view the numerical IDs for each group with the **id** command:
```bash
id <username>
```


## Cron jobs ...

## MD sphinx testing
Code blocks:
```python
for i in range(10):
    print(i)
```

Equation arrays:

$$
   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}
$$

A TODO list?:
- [ ] something 1
- [ ] something 2
- [x] Done 1

TODO list checkboxes are **not** displayed correctly in HTML created by sphinx....

### MD emojis are not handled by sphinx!?
This I find pretty weird to be honest....

:{notebook}:


:::{warning}
And here's a note with a colon fence!
:::

:{notebook}: :notebook: {:notebook:} :::{notebook}:::

This text includes a smily face |:smile:| and a snake too! |:snake:|

Don't you love it? |:heart_eyes:|