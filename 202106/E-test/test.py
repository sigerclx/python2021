import win32com.client
import tools
import configRead
speak = win32com.client.Dispatch('SAPI.SPVOICE')

speak.Speak("你好")