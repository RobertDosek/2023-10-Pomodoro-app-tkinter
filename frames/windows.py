def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProsessDpiAwareness(1)
    except:
        pass