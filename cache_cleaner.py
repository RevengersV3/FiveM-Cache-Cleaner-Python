import os
import shutil

def clear_fivem_cache():
    """
    Clears FiveM cache and browser data from local application directory.
    Returns True if successful, False otherwise.
    """
    try:
        # Define paths for FiveM cache and browser data
        paths = {
            'cache': os.path.join(os.getenv('LOCALAPPDATA'), 'FiveM', 'FiveM.app', 'cache'),
            'browser': os.path.join(os.getenv('LOCALAPPDATA'), 'FiveM', 'FiveM.app', 'browser')
        }
        
        # Check if paths exist
        paths_exist = any(os.path.exists(path) for path in paths.values())
        if not paths_exist:
            print("FiveM directories not found. Please verify FiveM is installed correctly.")
            return False
            
        # Clear each directory
        for name, path in paths.items():
            if os.path.exists(path):
                shutil.rmtree(path)
                print(f"Successfully cleared {name} directory.")
            else:
                print(f"{name.capitalize()} directory not found, skipping...")
        
        print("\nCache clearing completed successfully!")
        return True
        
    except PermissionError:
        print("Error: Permission denied. Please run the script as administrator.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while clearing cache: {str(e)}")
        return False

if __name__ == "__main__":
    print("FiveM Cache Cleaner")
    print("===================")
    
    # Ask for confirmation
    response = input("This will clear FiveM cache and browser data. Continue? (y/n): ").lower()
    
    if response == 'y':
        if clear_fivem_cache():
            print("\nOperation completed successfully.")
        else:
            print("\nOperation failed. Please check the error messages above.")
    else:
        print("\nOperation cancelled by user.")
    
    input("\nPress Enter to exit...")
