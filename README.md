Here’s the improved section in proper **Markdown (`.md`) format** for your `README.md`:

````markdown
## Notes & Customization

🚧 **This plugin is a work in progress.**  
I'm still learning how to build Flow Launcher plugins and also have limited experience with Python. However, the basic functionality is working as intended for now.

### ⚙️ System-Specific Configuration

This plugin has been built and tested with system-specific paths, including:

- The location of the **Sublime Text executable** on my PC.
- The **directories** I want to open in Sublime Text via the plugin.

Because of this, the plugin might not work out-of-the-box on your machine. You’ll need to make the following changes in the `main.py` file:

1. **Update the path to your Sublime Text executable**
2. **Modify the folder paths** that you want to open in Sublime

### 📁 Plugin Setup Instructions

1. **Download or clone** this repository.
2. **Make the necessary path changes** mentioned above.
3. **Paste the entire plugin folder** into the Flow Launcher plugins directory:

```plaintext
C:\Users\<YourUsername>\AppData\Roaming\FlowLauncher\Plugins
````

> **To find this directory:**
>
> * Open Flow Launcher
> * Go to *Settings → Installed Plugins*
> * Click on any non-default plugin
> * Click the small **folder icon** under the plugin name
> * File Explorer will open the plugin directory

```

Let me know if you'd like the full `README.md` compiled with this section integrated.
```
