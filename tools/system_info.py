import os
import platform
import psutil

def get_system_health():
    """
    Retrieves real-time system health metrics including CPU usage, 
    memory availability, and disk space. 
    Use this to diagnose performance issues or check local resources.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    health_report = {
        "os": f"{platform.system()} {platform.release()}",
        "cpu_usage_percent": cpu_usage,
        "memory_available_gb": round(memory.available / (1024**3), 2),
        "memory_used_percent": memory.percent,
        "disk_free_gb": round(disk.free / (1024**3), 2),
        "load_average": os.getloadavg() if hasattr(os, 'getloadavg') else "N/A"
    }
    
    return health_report

if __name__ == "__main__":
    # For testing the tool locally
    print(get_system_health())
