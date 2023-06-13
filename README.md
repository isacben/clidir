Classes:

- [x] BaseCommand Class (Protocol): to allow creation of Command classes
- [ ] Invoker Class: helps with calling (executing) the commands
- [ ] Controller (?): to initialize, find the Command classes, instantiate them and save them in a dictionary

```mermaid
flowchart TD
    subgraph "Developer's CLI main.py"
        a1[Get args]-->a2[Call the core]
    end

    a2-->A

    subgraph "Core: the CLI library"
        A[Parse arguments]-->B[Lookup command in filesystem]
        B-->C{Command?}
        C-->|Yes| D["Invoker parses/prepares\n the arguments"]
        C-->|No| F{Topic?}
        D-->E["Invoker calls the command"]
        F-->|Yes| G[Generate help for topic]
        F-->|No| I[Generate root help for app]
    end
    
    E-->J

    subgraph Developer's Command class
        J["Execute the command"]
    end
```


C-->D[Invoker.parse\n Parse args]
Invoker.run\n Call the Command.run method
B[Controller.init \n Instantiate commands and store them in a dictionary]
D-->E[Invoker.find\n Find the command]
    
    
    G-->I[Command.run\n Execute the command]