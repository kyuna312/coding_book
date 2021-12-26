#include <windows.h>
#include <stdio.h>
#include <string.h>
 
HANDLE hPort;
 
BOOL WriteByte(BYTE bybyte)
{
    DWORD iBytesWritten=0;
    DWORD iBytesToRead = 1;
    if(WriteFile(hPort,(LPCVOID) 
        &bybyte,iBytesToRead,&iBytesWritten,NULL)==0)
        return FALSE;
    else return TRUE;
}
 
BOOL WriteString(const void *instring, int length)
{
    int index;
    BYTE *inbyte = (BYTE *) instring;
    for(index = 0; index< length; ++index)
    {
        if (WriteByte(inbyte[index]) == FALSE)
            return FALSE;
    }
    return TRUE;
}
 
BOOL ReadByte(BYTE  &resp)
{
    BOOL bReturn = TRUE;
    BYTE rx;
    DWORD dwBytesTransferred=0;
 
    if (ReadFile (hPort, &rx, 1, &dwBytesTransferred, 0)> 0)
    {
        if (dwBytesTransferred == 1)
        {
            resp=rx;
            bReturn  = TRUE;
        }
        else bReturn = FALSE;
    }
    else    bReturn = FALSE;
    return bReturn;
}
 
BOOL ReadString(void *outstring, int *length)
{
    BYTE data;
    BYTE dataout[4096]={0};
    int index = 0;
    while(ReadByte(data)== TRUE)
    {
        dataout[index++] = data;
    }
    memcpy(outstring, dataout, index);
    *length = index;
    return TRUE;
}
 
void ClosePort()
{
    CloseHandle(hPort);
    return;
}
 
HANDLE ConfigureSerialPort(LPCSTR  lpszPortName)
{
    HANDLE hComm = NULL;
    DWORD dwError;
    DCB PortDCB;
    COMMTIMEOUTS CommTimeouts;

    hComm = CreateFile (lpszPortName, 
        GENERIC_READ | GENERIC_WRITE,

        0,             
        NULL,       
        OPEN_EXISTING, 
        0,             
        NULL);        

    PortDCB.DCBlength = sizeof (DCB);

    GetCommState (hComm, &PortDCB);

    PortDCB.BaudRate = 9600;           
    PortDCB.fBinary = TRUE;         
    PortDCB.fParity = TRUE;           
    PortDCB.fOutxCtsFlow = FALSE;      
    PortDCB.fOutxDsrFlow = FALSE;        
    PortDCB.fDtrControl = DTR_CONTROL_ENABLE;

    PortDCB.fDsrSensitivity = FALSE;     
    PortDCB.fTXContinueOnXoff = TRUE;  
    PortDCB.fOutX = FALSE;             
    PortDCB.fInX = FALSE;             
    PortDCB.fErrorChar = FALSE;      
    PortDCB.fNull = FALSE;        
    PortDCB.fRtsControl = RTS_CONTROL_ENABLE;

    PortDCB.fAbortOnError = FALSE;      

    PortDCB.ByteSize = 8;             
    PortDCB.Parity = NOPARITY;          
    PortDCB.StopBits = ONESTOPBIT;       
 
    if (!SetCommState (hComm, &PortDCB)){
        printf("Could not configure serial port\n");
        return NULL;
    }
    GetCommTimeouts (hComm, &CommTimeouts);
    CommTimeouts.ReadIntervalTimeout = MAXDWORD;
    CommTimeouts.ReadTotalTimeoutMultiplier = 0;
    CommTimeouts.ReadTotalTimeoutConstant = 0;
    CommTimeouts.WriteTotalTimeoutMultiplier = 0;
    CommTimeouts.WriteTotalTimeoutConstant = 0;
    if (!SetCommTimeouts (hComm, &CommTimeouts))
    {
        printf(" timeouts\n");
        return NULL;
    }
    return hComm;
}
 
int main(void){
    hPort = ConfigureSerialPort("COM1");
    if(hPort == NULL)
    {
        printf("configuration failed\n");
        return -1;
    }
    ClosePort();
    return 0;
}