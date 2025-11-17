# C# File I/O Cheat Sheet

## Including System.IO Namespace

```csharp
using System.IO;
```

## Filesystem-Related Classes in the System.IO Namespace

C# file operations are primarily handled through classes in the System.IO namespace:

- `File` - Static methods for file operations
- `FileInfo` - Instance methods for file operations
- `Directory` - Static methods for directory operations
- `DirectoryInfo` - Instance methods for directory operations
- `Path` - Utilities for working with file and directory paths
- `Stream` - Abstract base class for reading and writing bytes
- Various specialized streams: `FileStream`, `MemoryStream`, etc.
- Reader/Writer classes: `StreamReader`, `StreamWriter`, `BinaryReader`, `BinaryWriter`

## File Class (Static Methods)

### Reading Files
```csharp
// Read entire file as one string
string content = File.ReadAllText("path/to/file.txt");

// Read file as array of strings (one per line)
string[] lines = File.ReadAllLines("path/to/file.txt");

// Read file as bytes
byte[] data = File.ReadAllBytes("path/to/file.bin");
```

### Writing Files
```csharp
// Write string to file (overwrites if exists)
File.WriteAllText("path/to/file.txt", "Hello, World!");

// Write array of strings to file (one per line)
string[] lines = { "Line 1", "Line 2", "Line 3" };
File.WriteAllLines("path/to/file.txt", lines);

// Write bytes to file
byte[] data = { 0x48, 0x65, 0x6C, 0x6C, 0x6F }; // "Hello" in ASCII
File.WriteAllBytes("path/to/file.bin", data);

// Append to existing file
File.AppendAllText("path/to/file.txt", "Appended content");
```

### File Information
```csharp
// Check if file exists
bool exists = File.Exists("path/to/file.txt");

// Get last modified time
DateTime lastModified = File.GetLastWriteTime("path/to/file.txt");

// Get creation time
DateTime created = File.GetCreationTime("path/to/file.txt");

// Get file attributes
FileAttributes attrs = File.GetAttributes("path/to/file.txt");
bool isReadOnly = (attrs & FileAttributes.ReadOnly) == FileAttributes.ReadOnly;
```

### File Operations
```csharp
// Copy a file
File.Copy("source.txt", "destination.txt");
File.Copy("source.txt", "destination.txt", true); // Overwrite if exists

// Move/rename a file
File.Move("oldname.txt", "newname.txt");

// Delete a file
File.Delete("path/to/file.txt");
```

## FileInfo Class (Instance Methods)

```csharp
// Create a FileInfo object
FileInfo fileInfo = new FileInfo("path/to/file.txt");

// Get file properties
string name = fileInfo.Name;
string directory = fileInfo.DirectoryName;
long size = fileInfo.Length; // size in bytes
bool exists = fileInfo.Exists;
DateTime created = fileInfo.CreationTime;
DateTime modified = fileInfo.LastWriteTime;

// Operations
fileInfo.CopyTo("destination.txt");
fileInfo.MoveTo("newlocation.txt");
fileInfo.Delete();

// Create a new file and get a stream
using (FileStream fs = fileInfo.Create())
{
    // Work with the stream...
}

// Open file for reading
using (FileStream fs = fileInfo.OpenRead())
{
    // Read from stream...
}

// Open file for writing
using (FileStream fs = fileInfo.OpenWrite())
{
    // Write to stream...
}
```

## Directory Class (Static Methods)

```csharp
// Check if directory exists
bool exists = Directory.Exists("path/to/directory");

// Create directory
Directory.CreateDirectory("path/to/new/directory");

// Get files in a directory
string[] files = Directory.GetFiles("path/to/directory");
string[] txtFiles = Directory.GetFiles("path/to/directory", "*.txt");

// Get subdirectories
string[] dirs = Directory.GetDirectories("path/to/directory");

// Get current directory
string currentDir = Directory.GetCurrentDirectory();

// Delete directory
Directory.Delete("path/to/directory");         // Must be empty
Directory.Delete("path/to/directory", true);   // Recursive delete
```

## DirectoryInfo Class (Instance Methods)

```csharp
// Create a DirectoryInfo object
DirectoryInfo dirInfo = new DirectoryInfo("path/to/directory");

// Get directory properties
string name = dirInfo.Name;
string fullPath = dirInfo.FullName;
bool exists = dirInfo.Exists;
DateTime created = dirInfo.CreationTime;

// Get files and subdirectories
FileInfo[] files = dirInfo.GetFiles();
FileInfo[] txtFiles = dirInfo.GetFiles("*.txt");
DirectoryInfo[] subdirs = dirInfo.GetDirectories();

// Create a subdirectory
DirectoryInfo newSubdir = dirInfo.CreateSubdirectory("newSubdir");

// Delete
dirInfo.Delete();          // Must be empty
dirInfo.Delete(true);      // Recursive delete
```

## Path Class

```csharp
// Get file or directory name from path
string fileName = Path.GetFileName("C:/folder/file.txt");     // "file.txt"
string dirName = Path.GetDirectoryName("C:/folder/file.txt"); // "C:/folder"

// Get file extension
string ext = Path.GetExtension("file.txt");                   // ".txt"

// Get filename without extension
string name = Path.GetFileNameWithoutExtension("file.txt");   // "file"

// Combine paths (handles slashes properly)
string path = Path.Combine("folder", "subfolder", "file.txt");

// Get temporary filename
string tempFile = Path.GetTempFileName();

// Get temporary directory
string tempDir = Path.GetTempPath();

// Change extension
string newPath = Path.ChangeExtension("file.txt", ".doc");    // "file.doc"

// Get absolute path
string absPath = Path.GetFullPath("relative/path");

// Get path root
string root = Path.GetPathRoot("C:/folder/file.txt");         // "C:/"

// Get random filename
string randomName = Path.GetRandomFileName();
```

## StreamReader (Reading Text Files)

```csharp
// Create a StreamReader
using (StreamReader reader = new StreamReader("file.txt"))
{
    // Read entire file as string
    string allText = reader.ReadToEnd();
    
    // OR read line by line
    reader.BaseStream.Position = 0; // Reset position
    string line;
    while ((line = reader.ReadLine()) != null)
    {
        Console.WriteLine(line);
    }
}

// Read with specific encoding
using (StreamReader reader = new StreamReader("file.txt", Encoding.UTF8))
{
    // Read operations...
}
```

## StreamWriter (Writing Text Files)

```csharp
// Create a StreamWriter (overwrites existing file)
using (StreamWriter writer = new StreamWriter("file.txt"))
{
    writer.WriteLine("Line 1");
    writer.WriteLine("Line 2");
    writer.Write("No newline");
    writer.Write(" continued");
    
    // Force write to disk immediately
    writer.Flush();
}

// Append to file
using (StreamWriter writer = new StreamWriter("file.txt", append: true))
{
    writer.WriteLine("Appended line");
}

// Write with specific encoding
using (StreamWriter writer = new StreamWriter("file.txt", append: false, encoding: Encoding.UTF8))
{
    // Write operations...
}
```

## FileStream (Low-level File Access)

```csharp
// Create a new file and open for writing
using (FileStream fs = new FileStream("file.bin", FileMode.Create))
{
    byte[] data = { 0x48, 0x65, 0x6C, 0x6C, 0x6F }; // "Hello" in ASCII
    fs.Write(data, 0, data.Length);
}

// Open existing file for reading
using (FileStream fs = new FileStream("file.bin", FileMode.Open, FileAccess.Read))
{
    byte[] buffer = new byte[1024];
    int bytesRead = fs.Read(buffer, 0, buffer.Length);
    Console.WriteLine($"Read {bytesRead} bytes");
}

// Append to file
using (FileStream fs = new FileStream("file.bin", FileMode.Append))
{
    byte[] data = { 0x21 }; // "!" in ASCII
    fs.Write(data, 0, data.Length);
}
```

## BinaryReader/BinaryWriter

```csharp
// Write binary data
using (FileStream fs = new FileStream("data.bin", FileMode.Create))
using (BinaryWriter writer = new BinaryWriter(fs))
{
    writer.Write(42);              // Write Int32
    writer.Write(3.14159);         // Write Double
    writer.Write("Hello");         // Write String
    writer.Write(true);            // Write Boolean
    writer.Write((byte)255);       // Write Byte
}

// Read binary data
using (FileStream fs = new FileStream("data.bin", FileMode.Open))
using (BinaryReader reader = new BinaryReader(fs))
{
    int intValue = reader.ReadInt32();
    double doubleValue = reader.ReadDouble();
    string stringValue = reader.ReadString();
    bool boolValue = reader.ReadBoolean();
    byte byteValue = reader.ReadByte();
}
```

## Exception Handling

```csharp
try
{
    string content = File.ReadAllText("nonexistent.txt");
}
catch (FileNotFoundException ex)
{
    Console.WriteLine($"File not found: {ex.Message}");
}
catch (IOException ex)
{
    Console.WriteLine($"I/O error: {ex.Message}");
}
catch (UnauthorizedAccessException ex)
{
    Console.WriteLine($"Access denied: {ex.Message}");
}
catch (Exception ex)
{
    Console.WriteLine($"Error: {ex.Message}");
}
finally
{
    // Code that always runs
    Console.WriteLine("This always executes");
}
```

## Common File Operations

### CSV Processing

```csharp
// Reading CSV
string[] lines = File.ReadAllLines("data.csv");
foreach (string line in lines)
{
    string[] parts = line.Split(',');
    // Process each part
}

// Writing CSV
List<string> csvLines = new List<string>();
csvLines.Add("Name,Age,Email");
csvLines.Add("John,30,john@example.com");
csvLines.Add("Jane,25,jane@example.com");
File.WriteAllLines("output.csv", csvLines);
```

### File Monitoring

```csharp
// Watch for file changes in a directory
using (FileSystemWatcher watcher = new FileSystemWatcher())
{
    watcher.Path = @"C:\folder";
    watcher.NotifyFilter = NotifyFilters.LastWrite | NotifyFilters.FileName;
    watcher.Filter = "*.txt";
    
    // Add event handlers
    watcher.Changed += OnFileChanged;
    watcher.Created += OnFileCreated;
    watcher.Deleted += OnFileDeleted;
    watcher.Renamed += OnFileRenamed;
    
    // Begin watching
    watcher.EnableRaisingEvents = true;
    
    // Wait for user input to exit
    Console.WriteLine("Press 'q' to quit");
    while (Console.Read() != 'q') ;
}

// Event handlers
void OnFileChanged(object sender, FileSystemEventArgs e)
{
    Console.WriteLine($"File {e.Name} changed");
}

void OnFileCreated(object sender, FileSystemEventArgs e)
{
    Console.WriteLine($"File {e.Name} created");
}

void OnFileDeleted(object sender, FileSystemEventArgs e)
{
    Console.WriteLine($"File {e.Name} deleted");
}

void OnFileRenamed(object sender, RenamedEventArgs e)
{
    Console.WriteLine($"File renamed from {e.OldName} to {e.Name}");
}
```
