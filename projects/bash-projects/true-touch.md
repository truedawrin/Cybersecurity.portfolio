# 🛠️ True Touch

**True Touch** is a Bash-based utility designed to make creating multiple files and directories faster and easier.

Instead of manually running `touch` and `mkdir` commands repeatedly, True Touch uses a few simple prompts to let the user **mass-produce files and directories in one go**.

### ⚡ What It Does

True Touch allows you to:

* 📄 Create multiple files at once
* 📁 Create multiple directories at once
* ⚙️ Automate repetitive `touch` and `mkdir` tasks
* 💻 Perform everything directly from the terminal
* 🧑‍💻 Use a simple interactive prompt-based interface

The goal of the project is to turn repetitive filesystem tasks into a **quick and simple automated process** using Bash.

> **Less typing. More automation.**


```
#!/usr/bin/env bash

# ---------------------------------------
# True Touch
# Mass file & directory creator
# ---------------------------------------

echo "How many items do you want to create?"
read count

for (( i=1; i<=count; i++ ))
do
    echo ""
    echo "--- Item $i of $count ---"
    echo "What do you want to create? (file/dir)"
    read choice

    if [ "$choice" == "file" ]; then

        echo "Enter the file name (without extension):"
        read filename

        echo "Enter the file type/extension (e.g. txt, sh, py, md):"
        read filetype

        fullname="$filename.$filetype"

        if [ -e "$fullname" ]; then
            echo "A file named '$fullname' already exists. Skipping."
        else
            touch "$fullname"
            echo "File '$fullname' created successfully."
        fi

    elif [ "$choice" == "dir" ]; then

        echo "Enter the directory name:"
        read dirname

        if [ -e "$dirname" ]; then
            echo "A directory named '$dirname' already exists. Skipping."
        else
            mkdir "$dirname"
            echo "Directory '$dirname' created successfully."
        fi

    else
        echo "Invalid choice. Skipping this item."
    fi
done

echo ""
echo "Done. $count item(s) processed."
```

## Showcase

[screenshot](projects/bash-projects/images/image2.png)
