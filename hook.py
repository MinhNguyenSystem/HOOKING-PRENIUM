

# Tool HookLibrary (PRENIUM)
# COPYRIGHT: MinhNguyen2412
# CRE: --MinhNguyen2412-- vs --KhanhNguyen9872--
def clear_():__import__('os').system("cls" if __import__('os').name == "nt" else "clear")
clear_()
try:
    __import__('sys').stdout.write("$ ")
    __import__('sys').stdout.flush()
    __import__('time').sleep(0.05)
    __import__('sys').stdout.write("sh -c \"python3 __main__.py\"\n")
    __import__('sys').stdout.flush()
    __import__('time').sleep(0.1)
    __import__('sys').setrecursionlimit(999999999)
except:pass
try:
    data_requests = r'''
"""
requests.api
~~~~~~~~~~~~

This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.
"""

from . import sessions


def request(method, url, **kwargs):
    """Constructs and sends a :class:`Request <Request>`.

    :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    Usage::

      >>> import requests
      >>> req = requests.request('GET', 'https://httpbin.org/get')
      >>> req
      <Response [200]>
    """

    # By using the 'with' statement we are sure the session is closed, thus we
    # avoid leaving sockets open which can trigger a ResourceWarning in some
    # cases, and look like a memory leak in others.
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)


def get(url, params=None, **kwargs):
    r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    return request("get", url, params=params, **kwargs)


def options(url, **kwargs):
    r"""Sends an OPTIONS request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return request("options", url, **kwargs)


def head(url, **kwargs):
    r"""Sends a HEAD request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes. If
 B       `allow_redirects` is not provided, it will be set to `False` (as
        opposed to the default :meth:`request` behavior).
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    kwargs.setdefault("allow_redirects", False)
    return request("head", url, **kwargs)


def post(url, data=None, json=None, **kwargs):
    r"""Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
B    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    return request("post", url, data=data, json=json, **kwargs)


def put(url, data=None, **kwargs):
    r"""Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return request("put", url, data=data, **kwargs)


def patch(url, data=None, **kwargs):
    r"""Sends a PATCH request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return request("patch", url, data=data, **kwargs)


def delete(url, **kwargs):
    r"""Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return request("delete", url, **kwargs)

'''
except:pass
# try:
   # check = __import__('requests').get('http://www.python.org', timeout=5)
   # requests_dir = __import__('os').path.dirname(__import__('requests').__file__)
   # file_check = __import__('os').path.join(requests_dir, 'ㅤㅤㅤㅤ')
   # if __import__('os').path.isfile(file_check):
       # if __import__('os').path.join(requests_dir, 'api.py'):
           # try:__import__('os').unlink(__import__('os').path.join(requests_dir, 'api.py'))
           # except:pass
           # finally:pass
           # __import__('os').rename(file_check, __import__('os').path.join(requests_dir, 'api.py'))
# except (ImportError,ModuleNotFoundError) as e:
   # if "cannot import name 'delete' from 'requests.api'" in str(e) or "No module named 'requests.api'" in str(e) or "No module named 'requests.api'" in str(e):
       # error_message = str(e)
       # start = error_message.find('(')
       # end = error_message.find(')')
       # if start != -1 and end != -1:
           # path_ = error_message[start + 1:end]
           # _path = path_.replace('/api.py', '')
           # __import__('shutil').rmtree(_path)
       # print('[!] [ERROR: requests]\n>> INSTALL REQUESTS: pip uninstall requests -y && pip install requests')
   # else:print('[!] [ERROR: requests]\n>> INSTALL REQUESTS: pip install requests')
   # try:__import__('sys').exit(0)
   # except:__import__('sys').exit(0)
   # finally:__import__('sys').exit(exit())
# except (__import__('requests').ConnectionError,__import__('requests').Timeout):
   # print("[!] [PLEASE CONNECT TO THE NETWORK]")
   # try:__import__('sys').exit(0)
   # except:__import__('sys').exit(0)
   # finally:__import__('sys').exit(exit())
# try:api = __import__('os').path.join(__import__('os').path.dirname(__import__('requests').__file__), 'api.py')
# except NameError as e:
   # if "name 'requests' is not defined" in str(e):
       # print('[!] [YOU ARE NOT CONNECTED TO THE NETWORK]')
       # try:__import__('sys').exit(0)
       # except:__import__('sys').exit(0)
       # finally:__import__('sys').exit(exit())
LIBRARIES = ["colorama", "rich", "requests", "autopep8"]
try:
   from Crypto.Cipher import AES # type: ignore
except ImportError:
   print('INSTALL MODULE Crypto: pip install pycryptodome')
   __import__('sys').exit(1)
try:
    for LIB in LIBRARIES:
        try:
            __import__(LIB)
        except ImportError:
            print(f"INSTALLING LIBRARY IN PROGRESS: [{LIB}]")
            try:
                start_time = __import__('time').time()
                process = __import__('subprocess').Popen([__import__('sys').executable, "-m", "pip", "install", LIB], stdout=__import__('subprocess').PIPE, stderr=__import__('subprocess').PIPE)
                while True:
                    return_code = process.poll()
                    if return_code is not None:
                        if return_code == 0:
                            print()
                            print(f"SUCCESS .. [{LIB}]")
                        else:
                            print()
                            print(f"FAILURE .. {LIB}. VUI LÒNG THỬ LẠI SAU.")
                            print(process.stderr.read().decode())
                        break
                    current_time = __import__('time').time()
                    elapsed_time = current_time - start_time
                    print(f"Installing {LIB}... [{elapsed_time:.2f}s]", end='\r')
                    __import__('time').sleep(0.1)
            except Exception as e:
                print(f"AN ERROR APPEARED DURING INSTALLATION {LIB}: {e}")
                __import__('sys').exit(1)
            clear_()
except:pass
try:
    __import__('sys').setrecursionlimit(1500)
    from rich.console import Console # type: ignore
    from rich.syntax import Syntax # type: ignore
    import sys
except:pass
__pypath__ = __import__('os').getcwd()
PYTHONVERSION = ".".join(__import__('sys').version.split(" ")[0].split(".")[:-1])
__builtins__.bbllaacckk_stdout__ = __import__('sys').stdout
def BYPASS_IMPORT():
    cmd = '#'*42
    original_functions = {}
    def bypass_function(*args, **kwargs):
        print(f"[!] [ITS INGREDIENTS: {args}]")
        return None
    def make_wrapped_function(library_name, function_name):
        def wrapped_function(*args, **kwargs):
            if not any(str(keyword) in str(args[0]) for keyword in ["__pycache__", "MinhNguyen2412", "HOOKING", "_convert", "clear", "tmp", "cls", "ㅤㅤㅤ"]):
                _user_ = input(f"""{'='*42}
[!] [LIBRARY DISCOVERY ({library_name}.{function_name})]
[+] [R] TO RESTORE AND CONTINUE
[+] [B] TO BYPASS IT AND CONTINUE
[+] [X] TO EXIT: """).strip().upper()
                if _user_ == 'R':
                    print(f"[!] [RESTORING ({library_name}.{function_name})]")
                    return original_functions[library_name][function_name](*args, **kwargs)
                elif _user_ == 'B':
                    print(f"[!] [Bypassing ({library_name}.{function_name})]")
                    return bypass_function(*args, **kwargs)
                elif _user_ == 'X':
                    print("[!] [EXITING PROGRAM]")
                    raise SystemExit()
                else:
                    print("[!] [BYPASSING FUNCTION BY DEFAULT]")
                    return bypass_function(*args, **kwargs)
            else:return original_functions[library_name][function_name](*args, **kwargs)
        return wrapped_function
    def bypass_library(library_name, function_names):
        try:
            imported_lib = __import__(library_name)
            for function_name in function_names:
                if function_name in dir(imported_lib):
                    if library_name not in original_functions:
                        original_functions[library_name] = {}
                    original_functions[library_name][function_name] = getattr(imported_lib, function_name)
                    wrapped_function = make_wrapped_function(library_name, function_name)
                    setattr(imported_lib, function_name, wrapped_function)
        except ImportError:
            print(f"[!] [ERROR: LIBRARY ({library_name}) NOT FOUND]")
    libraries_to_bypass = {
        'telebot': ['TeleBot'],
        'os': ['remove', 'system', 'unlink'],
        'shutil': ['rmtree']
    }
    while True:
        clear_()
        print(cmd)
        for library, functions in libraries_to_bypass.items():
            print(f"[+] LIBRARY: {library} -> {functions}")
        _update_ = input(f"""{cmd}
>> ADD BYPASS LIBRARIES <<
[+] [Y] TO ADD MORE LIBRARIES
[+] [N] TO SKIP AND CONTINUE
[?] ==> """).strip().upper()
        if _update_ == 'Y':
            while True:
                print(cmd)
                _library_ = input("[+] [NAME LIBRARY BYPASS]: ").strip()
                try:__import__(_library_)
                except (ModuleNotFoundError, ValueError):
                    print("[!] [ERROR: LIBRARY IS NOT INSTALLED]")
                    continue
                _functions_ = input("[+] [FUNC LIBRARY (EX: remove, unlink,..)]: ").strip().split(',')
                try:
                    for func in _functions_:
                        if not hasattr(__import__(_library_), func.strip()):raise AttributeError
                    libraries_to_bypass[_library_] = [func.strip() for func in _functions_]
                    input(f"[+] ADDED LIBRARY: {_library_} -> {libraries_to_bypass[_library_]}")
                    break
                except AttributeError:
                    print("[!] [ERROR: FUNCTION IS NOT CORRECT WITH LIBRARY]")
                    continue
        elif _update_ == 'N':
            clear_()
            break
        else:continue
    for library, functions in libraries_to_bypass.items():
        bypass_library(library, functions)
console = Console()
dk_dis = []
dk_view = []
class HOOKING:
    def __init__(self):
        self.func = ["__class__", "__dir__", "__dict__", "__call__", "__repr__", "__abstractmethods__", "__annotations__"]
        self.____ = ("0000" + "".join([__import__("random").choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(10)]) + "E0" if __import__('os').name == 'nt' else "7f83" + "".join([__import__("random").choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(6)]) + "e0")
        try:__import__('shutil').rmtree(f"HOOKING")
        except:pass
        self.opcode = []
        self.key = None
        self.value = []
        self.var1 = []
        self.var2 = []
        self._FILE_ = 'HOOKING'
        if not __import__('os').path.exists(self._FILE_):__import__('os').makedirs(self._FILE_)
    class CTOCEntry:
        def __init__(self, position, cmprsdDataSize, uncmprsdDataSize, cmprsFlag, typeCmprsData, name):
            self.position = position
            self.cmprsdDataSize = cmprsdDataSize
            self.uncmprsdDataSize = uncmprsdDataSize
            self.cmprsFlag = cmprsFlag
            self.typeCmprsData = typeCmprsData
            self.name = name
    class PyInstArchive:
        PYINST20_COOKIE_SIZE = 24
        PYINST21_COOKIE_SIZE = 24 + 64
        MAGIC = b'MEI\014\013\012\013\016'
        def __init__(self, path):
            self.filePath = path
            self.pycMagic = b'\0' * 4
            self.barePycList = []
        def open(self):
            try:
                self.fPtr = open(self.filePath, 'rb')
                self.fileSize = __import__('os').stat(self.filePath).st_size
            except:
                print('[!] [ERROR: CAN NOT OPEN {0}]'.format(self.filePath))
                return False
            return True
        def close(self):
            try:self.fPtr.close()
            except:pass
        def checkFile(self):
            print('[+] [PROCESSING... {0}]'.format(self.filePath))
            searchChunkSize = 8192
            endPos = self.fileSize
            self.cookiePos = -1
            if endPos < len(self.MAGIC):
                print('[!] [ERROR: FILE IS TOO SHORT OR TRUNCATED]')
                return False
            while True:
                startPos = endPos - searchChunkSize if endPos >= searchChunkSize else 0
                chunkSize = endPos - startPos
                if chunkSize < len(self.MAGIC):break
                self.fPtr.seek(startPos, __import__('os').SEEK_SET)
                data = self.fPtr.read(chunkSize)
                offs = data.rfind(self.MAGIC)
                if offs != -1:
                    self.cookiePos = startPos + offs
                    break
                endPos = startPos + len(self.MAGIC) - 1
                if startPos == 0:break
            if self.cookiePos == -1:
                print('[!] [ERROR: THIS DUMP VERSION IS NOT SUPPORTED OR CANNOT DUMP...]')
                return False
            self.fPtr.seek(self.cookiePos + self.PYINST20_COOKIE_SIZE, __import__('os').SEEK_SET)
            if b'python' in self.fPtr.read(64).lower():self.pyinstVer = 21
            else:self.pyinstVer = 20
            return True
        def getCArchiveInfo(self):
            try:
                if self.pyinstVer == 20:
                    self.fPtr.seek(self.cookiePos, __import__('os').SEEK_SET)
                    (magic, lengthofPackage, toc, tocLen, pyver) = \
                    __import__('struct').unpack('!8siiii', self.fPtr.read(self.PYINST20_COOKIE_SIZE))
                elif self.pyinstVer == 21:
                    self.fPtr.seek(self.cookiePos, __import__('os').SEEK_SET)
                    (magic, lengthofPackage, toc, tocLen, pyver, pylibname) = \
                    __import__('struct').unpack('!8sIIii64s', self.fPtr.read(self.PYINST21_COOKIE_SIZE))
            except:
                print('[!] [ERROR: FILE CANNOT BE A STORAGE FOLDER...]')
                return False
            self.pymaj, self.pymin = (pyver//100, pyver%100) if pyver >= 100 else (pyver//10, pyver%10)
            print('[+] [PYTHON VERSION]: {0}.{1}'.format(self.pymaj, self.pymin))
            tailBytes = self.fileSize - self.cookiePos - (self.PYINST20_COOKIE_SIZE if self.pyinstVer == 20 else self.PYINST21_COOKIE_SIZE)
            self.overlaySize = lengthofPackage + tailBytes
            self.overlayPos = self.fileSize - self.overlaySize
            self.tableOfContentsPos = self.overlayPos + toc
            self.tableOfContentsSize = tocLen
            return True
        def parseTOC(self):
            self.fPtr.seek(self.tableOfContentsPos, __import__('os').SEEK_SET)
            self.tocList = []
            parsedLen = 0
            while parsedLen < self.tableOfContentsSize:
                (entrySize, ) = __import__('struct').unpack('!i', self.fPtr.read(4))
                nameLen = __import__('struct').calcsize('!iIIIBc')
                (entryPos, cmprsdDataSize, uncmprsdDataSize, cmprsFlag, typeCmprsData, name) = \
                __import__('struct').unpack( \
                    '!IIIBc{0}s'.format(entrySize - nameLen), \
                    self.fPtr.read(entrySize - 4))
                try:name = name.decode("utf-8").rstrip("\0")
                except UnicodeDecodeError:
                    newName = str(__import__('uuid4').uuid())
                    print('[!] [WARNING: FILE NAME {0} CONTAINS INVALID BYTES. USE RANDOM NAMES]: {1}'.format(name, newName))
                    name = newName
                if name.startswith("/"):name = name.lstrip("/")
                if len(name) == 0:
                    name = str(__import__('uuid4').uuid())
                    print('[!] [WARNING: AN UNNAMED FILE FOUND IN CARCHIVE. USE RANDOM NAMES]: {0}'.format(name))
                self.tocList.append(HOOKING.CTOCEntry(self.overlayPos + entryPos,cmprsdDataSize,uncmprsdDataSize,cmprsFlag,typeCmprsData,name))
                parsedLen += entrySize
        def _writeRawData(self, filepath, data):
            nm = filepath.replace('\\', __import__('os').path.sep).replace('/', __import__('os').path.sep).replace('..', '__')
            nmDir = __import__('os').path.dirname(nm)
            if nmDir != '' and not __import__('os').path.exists(nmDir):__import__('os').makedirs(nmDir)
            open(nm, 'wb').write(data)
        def extractFiles(self):
            print('[+] [DECOMPRESSION PROCEDURE...PLEASE WAIT]')
            extractionDir = __import__('os').path.join(__import__('os').getcwd(), __import__('os').path.basename(self.filePath) + '-dump_exe')
            if not __import__('os').path.exists(extractionDir):__import__('os').mkdir(extractionDir)
            __import__('os').chdir(extractionDir)
            for entry in self.tocList:
                self.fPtr.seek(entry.position, __import__('os').SEEK_SET)
                data = self.fPtr.read(entry.cmprsdDataSize)
                if entry.cmprsFlag == 1:
                    try:data = __import__('zlib').decompress(data)
                    except __import__('zlib').error:
                        print('[!] [ERROR: CANNOT DECOMPRESS {0}]'.format(entry.name))
                        continue
                    assert len(data) == entry.uncmprsdDataSize
                if entry.typeCmprsData == b'd' or entry.typeCmprsData == b'o':continue
                basePath = __import__('os').path.dirname(entry.name)
                if basePath != '':
                    if not __import__('os').path.exists(basePath):__import__('os').makedirs(basePath)
                if entry.typeCmprsData == b's':
                    print('[+] [EXECUTABLE FILE]: {0}.pyc'.format(entry.name))
                    if self.pycMagic == b'\0' * 4:self.barePycList.append(entry.name + '.pyc')
                    self._writePyc(entry.name + '.pyc', data)
                elif entry.typeCmprsData == b'M' or entry.typeCmprsData == b'm':
                    if data[2:4] == b'\r\n':
                        if self.pycMagic == b'\0' * 4: self.pycMagic = data[0:4]
                        self._writeRawData(entry.name + '.pyc', data)
                    else:
                        if self.pycMagic == b'\0' * 4:self.barePycList.append(entry.name + '.pyc')
                        self._writePyc(entry.name + '.pyc', data)
                else:
                    self._writeRawData(entry.name, data)
                    if entry.typeCmprsData == b'z' or entry.typeCmprsData == b'Z':self._extractPyz(entry.name)
            self._fixBarePycs()
        def _fixBarePycs(self):
            for pycFile in self.barePycList:open(pycFile, 'r+b').write(self.pycMagic)
        def _writePyc(self, filename, data):
            with open(filename, 'wb') as pycFile:
                pycFile.write(self.pycMagic) 
                if self.pymaj >= 3 and self.pymin >= 7:
                    pycFile.write(b'\0' * 4)
                    pycFile.write(b'\0' * 8) 
                else:
                    pycFile.write(b'\0' * 4)
                    if self.pymaj >= 3 and self.pymin >= 3:pycFile.write(b'\0' * 4)
                pycFile.write(data)
        def _extractPyz(self, name):
            dirName =  name + '-dump_exe'
            if not __import__('os').path.exists(dirName):__import__('os').mkdir(dirName)
            with open(name, 'rb') as f:
                pyzMagic = f.read(4)
                assert pyzMagic == b'PYZ\0' 
                pyzPycMagic = f.read(4)
                if self.pycMagic == b'\0' * 4:self.pycMagic = pyzPycMagic
                elif self.pycMagic != pyzPycMagic:
                    self.pycMagic = pyzPycMagic
                    print('[!] [WARNING: PYC FILE OF FILE IN PYZ ARCHIVE DIFFERENT FROM FILE IN CARCHIVE]')
                if self.pymaj != __import__('sys').version_info.major or self.pymin != __import__('sys').version_info.minor:
                    print(f'[!] [WARNING: THIS TOOL IS THE PYTHON VERSION {self.pymaj}.{self.pymin}]\n[!] [NOT SUITABLE FOR CURRENT VERSION.]' )
                    print('[+] [SKIP EXTRACTING PYZ]')
                    return
                (tocPosition, ) = __import__('struct').unpack('!i', f.read(4))
                f.seek(tocPosition, __import__('os').SEEK_SET)
                try:toc = __import__('marshal').load(f)
                except:
                    print('[!] [ERROR: DUMP FAILED.]\n[!] [ERROR: UNABLE TO EXTRACT {0}].\n[+] [EXPLORING THE REMAINING FILES.]'.format(name))
                    return
                print('[+] [FILE {0} FOUND IN PYZ ARCHIVE]'.format(len(toc)))
                if type(toc) == list:toc = dict(toc)
                for key in toc.keys():
                    (ispkg, pos, length) = toc[key]
                    f.seek(pos, __import__('os').SEEK_SET)
                    fileName = key
                    try:fileName = fileName.decode('utf-8')
                    except:pass
                    fileName = fileName.replace('..', '__').replace('.', __import__('os').path.sep)
                    if ispkg == 1:filePath = __import__('os').path.join(dirName, fileName, '__init__.pyc')
                    else:filePath = __import__('os').path.join(dirName, fileName + '.pyc')
                    fileDir = __import__('os').path.dirname(filePath)
                    if not __import__('os').path.exists(fileDir):__import__('os').makedirs(fileDir)
                    try:
                        data = f.read(length)
                        data = __import__('zlib').decompress(data)
                    except:
                        print('[!] [ERROR: CANNOT BE EXPRESSED {0}, MAY BE ENCRYPTED.]\n[+] [UNCOMPRESS AS OLD.]'.format(filePath))
                        open(filePath + '.encrypted', 'wb').write(data)
                    else:self._writePyc(filePath, data)
    class Crack_Hyperion:
        def get_code(self):return __import__('tokenize').untokenize(self.ntokens)
        def replace_var(self, target, var):
            self.ntokens = []
            for token in self.content:
                string = token.string
                if int(token.type) == 1:
                    if str(string) == str(target):
                        string = str(var)
                self.ntokens.append(__import__('tokenize').TokenInfo(token.type, string, token.start, token.end, token.line))
            self.put_code(self.get_code())
        def put_code(self, content):self.content = list(__import__('tokenize').tokenize(__import__('io').BytesIO(content).readline))
        def replace_vars(code, code_, _code):
            code = code.split(b"\n")
            for i in range(0, len(code), 1):
                if code_ in code[i]:
                    j = code[i]
                    for l in range(0, len(j), 1):
                        try:
                            if j[l:l+len(code_)] == code_:
                                if (j[l+len(code_):l+len(code_)+1] in globals()["mot_dong_string_rat_dai"]) or (j[l-1:l] in globals()["mot_dong_string_rat_dai"]):break
                                else:j = j[:l] + _code + j[l+len(code_):]
                        except IndexError:break
                    code[i] = j
            code = b"\n".join(code)
            return code
    __builtins__.Crack_Hyperion = Crack_Hyperion
    del Crack_Hyperion
    def DEOBF_HYPERION_V2(self,CODE):
        __import__('sys').executable = 'python.exe'
        global mot_dong_string_rat_dai
        VARS = CODE.decode()
        Folder_file = "VARS-HYPER"
        if __import__('os').path.exists(Folder_file):
            FILE_PATH = __import__('os').path.join(Folder_file, "_VARS.py")
            if __import__('os').path.exists(FILE_PATH):
                CODE = open(FILE_PATH, 'rb').read().split(b"\n")
            else:
                try:
                    if not __import__('os').listdir(Folder_file):
                        __import__('os').rmdir(Folder_file)
                except:pass
                CODE = VARS.encode().split(b"\n")
        ignore_var = False
        for love in range(0, len(CODE), 1):
            if b"from builtins import " in CODE[love]:
                l = love
                ignore_var = True
                break
        hey_you = 0
        line_removed = 0
        if b'locals()[' not in CODE[0]:
            print('[+] [REMOVE __license__ ...]')
            for love in range(0, len(CODE), 1):
                if b"locals()[" in CODE[love]:
                    CODE = CODE[love:]
                    hey_you = love
                    line_removed = love
                    break
        if ignore_var:
            print("[+] [CODE DETECTION, DEOBF START...]")
            love = b"\n".join(CODE[:l-hey_you])
            Faskm = b"\n".join(CODE[l-hey_you:])
            dump = False
        else:
            print("[+] [NO CODE DETECTED, ONLY DEOBF VARS....]")
            love = b"\n".join(CODE)
            Faskm = b"\n".join(CODE)
            dump = True
            print("[!] [ONLY DEOBF DOES NOT ENCOURAGE VARS OUTBREAK]")
            # while 1:
            #     hahaha = input("[+] [DO YOU WANT TO READ VARS? (Y/n)]: ").lower()
            #     if hahaha=="y":
            #         ignore_var=True
            #         break
            #     elif hahaha=="n":break
            print("[!] [ERROR: DEOBF CANNOT CONTINUE]")
            hahaha = 'n'
            if hahaha=="y":
                ignore_var=True
        if ignore_var:
            ignore_var = [
                '__cpy_syspath__',
                '__name__', 
                'exit',
                '__doc__',
                '__file__',
                '__cached__',
                '__package__',
                '__loader__',
                '__spec__',
                '__annotations__',
                '__builtins__',
                '__warningregistry__',
            ]
            print("[+] [ANTI __import__ ...]")
            chan_quyen_thoat_code = vars(__import__('sys')).copy()
            sys.exit = None
            __import__('builtins').exit = None
            exit = None
            modules_vip_pro = {}
            for i in ['os', 'threading', 'subprocess', 'sys']:
                try:
                    modules_vip_pro[i] = sys.modules[i]
                    sys.modules[i]=None
                except KeyError:pass
            love = love.split(b"\n")
            _max_ = len(love)
            _min_ = 0
            for i in love:
                try:
                    exec(i, globals())
                    __builtins__.index = int(love.index(i))+1
                    __builtins__.i=int((100/(_max_-_min_))*(__builtins__.index-_min_))
                    __builtins__.bbllaacckk_stdout__.write(f"\r[+] [%-25s] %d%% ({__builtins__.index}/{_max_})" % ('='*int(__builtins__.i/4), __builtins__.i))
                    __builtins__.bbllaacckk_stdout__.flush()
                except KeyboardInterrupt:
                    print('\n[!] [EXIT READ VARS (KeyboardInterrupt)]')
                    print(f'[!] at line {int(love.index(i))+line_removed+1} in code', end='')
                    break
                except Exception as e:
                    print(f'\n[!] [EXIT READ VARS SO]: {str(e)}')
                    print(f'[+] [at line {int(love.index(i))+line_removed+1} in code]', end='')
                    break
                except:
                    print('\n[!] [EXIT READ VARS SO]: unknown error')
                    print(f'[!] [at line {int(love.index(i))+line_removed+1} in code]', end='')
                    break
            print("\n[+] [READ VARS SUCCESS]")
            print("[+] [RESTORE IMPORT...]")
            for i in modules_vip_pro:
                try:sys.modules[i] = modules_vip_pro[i]
                except KeyError:pass
            exit = chan_quyen_thoat_code['exit']
            sys.exit = exit
            __import__('builtins').exit = exit
            love = {}
            hey_you = 1
            for hey_you in globals():
                if hey_you in ignore_var:continue
                elif hey_you in __import__('builtins').__dict__:continue
                love[hey_you] = globals()[hey_you]
            love=dict(sorted(love.items(),key=lambda x: (len(x[0]),len(x[0])),reverse=True))
            unhexlify_name = "__import__('binascii').unhexlify"
            eval_name = "eval"
            mot_dong_string_rat_dai = [str(char).encode() for char in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"]
            if dump:
                replace_type = 0
                print("[!] [ONLY DEOBF CODE, REPLACE VARS ARE NOT RECOMMENDED]")
                while 1:
                    hahaha = input("[+] [DO YOU WANT TO REPLACE VARS? (Y/n)]: ").lower()
                    if hahaha=="y":
                        dump=False
                        break
                    elif hahaha=="n":break
            else:
                while 1:
                    choose = str(input("""[+] [<REPLACE VAR...>]
[>] [1 - FAST (Low accuracy)]
[>] [2 - MIDDLE RANGE (High precision)]
[>] [3 - SKIP]: """))
                    if choose == "1":
                        replace_type = 0
                        break
                    elif choose == "2":
                        replace_type = 1
                        break
                    elif choose == "3":
                        dump = True
                        break
                del choose
            if not dump:
                print(f'[+] [REPLACE VARS STRING ({("Fast" if replace_type == 0 else "Very Slow")} mode)...]')
                if replace_type == 1:
                    deobf = __builtins__.Crack_Hyperion()
                    deobf.put_code(Faskm)
                __tmp_list__ = list(love)
                _max_ = len(__tmp_list__)
                _min_ = 0
                for hahaha in love:
                    if len(hahaha) >= 1:
                        if hahaha.encode() in Faskm:
                            __tmp_var__ = str(type(love[hahaha]))
                            if __tmp_var__ == "<class 'bool'>" or __tmp_var__ == "<class 'int'>" or __tmp_var__ == "<class 'float'>":fuck_you = str(love[hahaha])
                            elif __tmp_var__ == "<class 'function'>":fuck_you = str(love[hahaha]).split(" ")[1]
                            elif __tmp_var__ == "<class 'builtin_function_or_method'>":
                                __tmp_var__ = str(love[hahaha]).split(" ")[-1][:-1]
                                if __tmp_var__ == "unhexlify":__tmp_var__ = unhexlify_name
                                fuck_you = __tmp_var__
                            elif __tmp_var__ == "<class 'function'>":
                                fuck_you = str(love[hahaha])
                                if str(HOOKING.check_fun(fuck_you)) in str(fuck_you):continue
                                else:fuck_you = " ".join(str(fuck_you).split(" ")[:-2][-1:]) + f"() '''args: {str(love[hahaha].__code__.co_varnames)}'''"
                            elif __tmp_var__ == "<class 'type'>":fuck_you = str(love[hahaha]).split(" ")[1].split(".")[-1][:-2]
                            elif __tmp_var__ == "<class 'bytes'>":fuck_you = str(love[hahaha]).replace("\r","\\r").replace("\n","\\n").replace("\t","\\t")
                            else:fuck_you = str("\"" + str(love[hahaha]).replace('\\',r"\\").replace('"', '\\"') + "\"").replace("\n", "\\n").replace("\t","\\t").replace("\r","\\r").replace("\b","\\b").replace("\f","\\f")
                            if replace_type == 1:deobf.replace_var(hahaha, fuck_you)
                            elif replace_type == 0:Faskm = __builtins__.Crack_Hyperion.replace_vars(Faskm, hahaha.encode(), fuck_you.encode())
                    __builtins__.index = int(__tmp_list__.index(hahaha))+1
                    __builtins__.i=int((100/(_max_-_min_))*(__builtins__.index-_min_))
                    __builtins__.bbllaacckk_stdout__.write(f"\r[+] [%-25s] %d%% ({__builtins__.index}/{_max_} var)" % ('='*int(__builtins__.i/4), __builtins__.i))
                    __builtins__.bbllaacckk_stdout__.flush()
                __builtins__.bbllaacckk_stdout__.write(f"\r[+] [=========================] 100% ({_max_}/{_max_} var)")
                __builtins__.bbllaacckk_stdout__.flush()
                print("")
                if replace_type == 1:Faskm = deobf.get_code()
            if f"{unhexlify_name}(".encode() in Faskm:
                if input("[!] [DETECT BINASCII]\n[+] [DO YOU WANT TO DEOBF IT? (Y/n)]: ").lower() == 'y':
                    print('[+] [FIXING BINASCII (can take a long time)]...')
                    song_chet_co_so = f"{eval_name}({unhexlify_name}(".encode()
                    Faskm = Faskm.split(b"\n")
                    _max_ = len(Faskm)
                    _min_ = 0
                    skip_error = []
                    for hahaha in range(len(Faskm)):
                        if f"{unhexlify_name}(".encode() in Faskm[hahaha]:
                            ghe_vay_sao = Faskm[hahaha].split(b"=")
                            for love in range(len(ghe_vay_sao)):
                                if f"{unhexlify_name}(".encode() in ghe_vay_sao[love]:
                                    __tmp_var__ = ghe_vay_sao[love]
                                    max_attempts = 100
                                    attempt = 0
                                    successful = False
                                    while attempt < max_attempts:
                                        attempt += 1
                                        while __tmp_var__:
                                            if __tmp_var__[:len(eval_name) + len(unhexlify_name) + 2] == song_chet_co_so:
                                                while len(__tmp_var__) > len(eval_name) + len(unhexlify_name) + 2:
                                                    try:
                                                        if song_chet_co_so in __tmp_var__:
                                                            fuck_you = eval(__tmp_var__[5:-1]).encode()
                                                        else:
                                                            fuck_you = eval(__tmp_var__).encode()
                                                        fuck_you = ghe_vay_sao[love].replace(__tmp_var__, fuck_you)
                                                        successful = True
                                                        break
                                                    except Exception:__tmp_var__ = __tmp_var__[:-1]
                                                break
                                            elif __tmp_var__[:len(unhexlify_name) + 1] == song_chet_co_so:
                                                while len(__tmp_var__) > len(unhexlify_name) + 1:
                                                    try:
                                                        fuck_you = eval(__tmp_var__).encode()
                                                        fuck_you = ghe_vay_sao[love].replace(__tmp_var__, fuck_you)
                                                        successful = True
                                                        break
                                                    except Exception:__tmp_var__ = __tmp_var__[:-1]
                                                break
                                            else:__tmp_var__ = __tmp_var__[1:]
                                        if successful:break
                                        if f"{unhexlify_name}(".encode() in fuck_you:
                                            ghe_vay_sao[love] = fuck_you
                                            __tmp_var__ = fuck_you
                                            continue
                                        if not __tmp_var__:fuck_you = ghe_vay_sao[love]
                                        break
                                    if not successful:skip_error.append(hahaha + 1)
                                    ghe_vay_sao[love] = fuck_you
                            Faskm[hahaha] = b"=".join(ghe_vay_sao)
                        __builtins__.i = int((100 / (_max_ - _min_)) * (hahaha - _min_)) + 1
                        __builtins__.bbllaacckk_stdout__.write(f"\r[+] [%-25s] %d%% ({hahaha + 1}/{_max_} unhexlify)" % ('=' * int(__builtins__.i / 4), __builtins__.i))
                        __builtins__.bbllaacckk_stdout__.flush()
                    __builtins__.bbllaacckk_stdout__.write(f"\r[+] [=========================] 100% ({_max_}/{_max_} unhexlify)")
                    __builtins__.bbllaacckk_stdout__.flush()
                    print("")
                    print(f"[+] [SKIP VARS ERROR AT LINE {', '.join(map(str, skip_error))}]")
                    Faskm = b"\n".join(Faskm)
                else:Faskm = b"from binascii import unhexlify\n" + Faskm
                Faskm = Faskm.replace(unhexlify_name.encode(), b"unhexlify")
        return Faskm.decode()
    def CHECK_OPCODE(self,bytecode, deobf):
        if str(deobf) == 'kramer':
            try:
                byte = __import__('io').StringIO()
                op = __import__('sys').stdout
                __import__('sys').stdout = byte
                __import__('dis').dis(bytecode)
                __import__('sys').stdout = op
                ocode = byte.getvalue().splitlines()
            except:pass
            del byte,op
            for i in ocode:
                get = __import__('re').search(r'LOAD_CONST\s+1\s+\((\d{4,6})\)', i)
                if get:
                    self.key = get.group(1)
        for line in __import__('dis').get_instructions(bytecode):
            self.opcode.append(line)
        # print(__import__('dis').dis(bytecode))
        # print('\n'.join(map(str, opcode)))
        del bytecode
        if str(deobf) == 'specter':
            for line in self.opcode:
                if line.opname == 'LOAD_CONST':
                    if "<code object <lambda> at " not in str(line.argval) and 'None' not in str(line.argval) and "'*'" not in str(line.argval) and str(line.argval) != '0':
                        if "\\x0" not in str(line.argval):
                            self.key = line.argval
                            self.value.append(line.argval)
                        else:
                            self.value.append(line.argval)
                elif line.opname == 'STORE_NAME':
                    self.var1.append(line.argval)
                elif line.opname == 'LOAD_NAME':
                    if 'globals' not in str(line.argval):
                        self.var2.append(line.argval)
                    else:self.value.append(line.argval)
            return self.key, self.value, self.var1, self.var2
        elif str(deobf) == 'impostor':
            for line in self.opcode:
                if line.opname == 'LOAD_CONST' and isinstance(line.argval, str):
                    self.value.append(line.argval)
            return self.value[int(len(self.value[:-3]))]
        elif str(deobf) == 'kramer':
            for line in self.opcode:
                if line.opname == 'LOAD_CONST' and '/' in str(line.argval):
                    self.value.append(line.argval)
            return self.key, self.value
    def CLEAR_CODE(self,CODE):
        new_data = []
        for i in CODE:
            try:
                if "#" == i[0]:continue
            except IndexError:pass
            if not i.strip():continue
            new_data.append(i)
        return "\n".join(new_data)
    def CHECK_BYTE(self,CODE):
        i = 0
        for i in range(1, 101, 1):
            try:
                if "<code object <module>" in str(__import__('marshal').loads(CODE[i:])):
                    CODE = __import__('marshal').loads(CODE[i:])
                    break
                else:CODE = CODE.decode();break
            except:pass
        return CODE
    class Dec_AST:
        def CHECK_1(CODE, _1_):
            _2_ = _1_ + 1
            if _2_ < len(CODE):
                _3_ = CODE[_2_]
                if _3_:
                    _4_ = CODE[_2_:].split('\n', 1)[0]
                    return _4_
        def CHECK_2(CODE):
            _1_ = __import__('ast').parse(CODE)
            _2_ = []
            for _3_ in __import__('ast').walk(_1_):
                if isinstance(_3_, __import__('ast').Assign):
                    for _4_ in _3_.targets:
                        if isinstance(_4_, __import__('ast').Name) and _4_.id not in _2_:
                            if isinstance(_3_.value, __import__('ast').NameConstant) and _3_.value.value is None:_2_.append(_4_.id)
            return ''.join(_2_)
    def DEOBF_AST(self,CODE):
        CODE = CODE.decode()
        if 'type(*_);' not in CODE:
            return None
        _A_ = CODE.count(';')
        _B_ = CODE.rfind(';')
        if _A_ > 0:
            _C_ = HOOKING.Dec_AST.CHECK_1(CODE, _B_)
            _D_ = HOOKING.Dec_AST.CHECK_2(CODE)
            if _C_ and _D_:
                _E_ = __import__('marshal').dumps(compile(CODE.replace(f"{_C_}", f"print(__import__('ast').unparse({_D_}))").encode(),'MinhNguyen2412', 'exec'))
                del _A_,_B_,_C_,_D_
        with __import__('tempfile').NamedTemporaryFile(suffix='.py', delete=False) as DONE:DONE.write(("exec(__import__('marshal').loads("+str(_E_)+"))").encode())
        out = __import__('subprocess').run([__import__('sys').executable, DONE.name], capture_output=True, text=True)
        del CODE,_E_
        data = out.stdout.split('\n')
        result = self.CLEAR_CODE(data)
        del data
        __import__('os').unlink(DONE.name)
        return result
    def DEOBF_PYOBFUSCATE(self,CODE):
        CODE = CODE.decode()
        if 'lambda **kwargs' not in CODE:
            return None
        _A_ = []
        for _B_ in CODE.split('\n'):
            if 'lambda' in _B_ and not '**' in _B_:continue
            _A_.append(_B_.strip())
        FUNC = __import__('marshal').dumps(compile(r"""
{0}
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
try:
    if not 'exec' == pyobfuscate[0][1]:
        print('Try Another Method :)')
        input('Press Enter to Exit')
        exit()
    try:
        def a(i):return unpad(AES.new(__import__('hashlib').sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0]).encode()).digest()[:24], AES.MODE_CBC, i[:AES.block_size]).decrypt(i[AES.block_size:]), AES.block_size).decode()
        print(a(pyobfuscate[1][2]))
    except:
        def a(i):return unpad(AES.new(__import__('hashlib').sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0][:-1]).encode()).digest()[:24], AES.MODE_CBC, i[:AES.block_size]).decrypt(i[AES.block_size:]), AES.block_size).decode()
        print(a(pyobfuscate[1][2]))
except:
    def a(i, j):
        i = __import__('base64').b85decode(i)
        j, c = b(j, i[:8])
        return AES.new(j, AES.MODE_CFB, c).decrypt(i[8:]).decode()
    def b(i, j):
        k = __import__('hashlib').pbkdf2_hmac('sha256', i.encode(), j, 100000)
        return (k[:16], k[16:])
    print(a(list(obfuscate.values())[0], list(obfuscate.keys())[0][1:-1]))
""".format('\n'.join(_A_)).encode(),'MinhNguyen2412', 'exec'))
        with __import__('tempfile').NamedTemporaryFile(suffix='.py', delete=False) as _C_:_C_.write(("exec(__import__('marshal').loads("+str(FUNC)+"))").encode())
        out = __import__('subprocess').run([__import__('sys').executable, _C_.name], capture_output=True, text=True)
        del CODE,FUNC
        data = out.stdout.split('\n')
        result = self.CLEAR_CODE(data)
        del data
        __import__('os').unlink(_C_.name)
        return result
    def DEOBF_SPECTER(self,CODE):
        loc = __import__('re').findall(r"Func.calculate\(\d*?\)\s*?,Func.define\('__.*?__', b'(.*?)'\)", CODE.decode())
        key, value, var1, var2 = self.CHECK_OPCODE(__import__('marshal').loads(eval("+".join(["b'" + p + "'" for p in loc]))),deobf='specter')
        var1 = var1[:-1] 
        done = __import__('marshal').dumps(compile(f"""from builtins import *
{','.join(var1)}={', '.join(map(str, value))}
def MINHNGUYEN2412(CODER):
    return ''.join(chr(int(DEOBF)-int({key}))for DEOBF in CODER.decode().split('\\x00'))
(lambda DEOBF:globals()['print'](''.join(MINHNGUYEN2412(CODER=CODER)for CODER in DEOBF)))([{','.join(var2)}])
""".encode(),'MinhNguyen2412', 'exec'))
        with __import__('tempfile').NamedTemporaryFile(suffix='.py', delete=False) as DONE:DONE.write(("exec(__import__('marshal').loads("+str(done)+"))").encode())
        out = __import__('subprocess').run([__import__('sys').executable, DONE.name], capture_output=True, text=True)
        del CODE,loc,done
        data = out.stdout.split('\n')
        result = self.CLEAR_CODE(data)
        del data
        __import__('os').unlink(DONE.name)
        return result
    def DEOBF_KRAMER(self,CODE):
        key,value =  self.CHECK_OPCODE(self.CHECK_BYTE(CODE),deobf='kramer')
        done = __import__('marshal').dumps(compile(f"""class MINH_DEPTROAI():
 def __decode__(self:object,_execute:str)->exec:return(None,self._CODE_(_execute))[0]
 def __init__(self:object,_MODULE_:float=False,_VISUAL_CODE_:float=0,*_EM_:float,**_TÔI_:float)->exec:
  _MODULE_,self._CODE_,self._RỒI_,_TÔI_[_VISUAL_CODE_],self._EM_,self._YÊU_=lambda _MODULE_:exit()if self._EM_[15]+self._EM_[17]+self._EM_[8]+self._EM_[13]+self._EM_[19] in open(__file__, errors=self._EM_[8]+self._EM_[6]+self._EM_[13]+self._EM_[14]+self._EM_[17]+self._EM_[4]).read() or self._EM_[8]+self._EM_[13]+self._EM_[15]+self._EM_[20]+self._EM_[19] in open(__file__, errors=self._EM_[8]+self._EM_[6]+self._EM_[13]+self._EM_[14]+self._EM_[17]+self._EM_[4]).read()else"".join(_MODULE_ if _MODULE_ not in self._EM_ else self._EM_[self._EM_.index(_MODULE_)+1 if self._EM_.index(_MODULE_)+1<len(self._EM_)else 0]for _MODULE_ in "".join(chr(ord(t)-{key})if t!="ζ"else"\\n"for t in self._RỒI_(_MODULE_))),lambda _NHƯ_:self._YÊU_(_MODULE_(_NHƯ_)),lambda _NHƯ_:"".join(__import__(self._EM_[1]+self._EM_[8]+self._EM_[13]+self._EM_[0]+self._EM_[18]+self._EM_[2]+self._EM_[8]+self._EM_[8]).unhexlify(str(_MẤT_)).decode()for _MẤT_ in str(_NHƯ_).split('/')),eval,exit()if _MODULE_ else'abcdefghijklmnopqrstuvwxyz0123456789',lambda _MODULE_:str(_TÔI_[_VISUAL_CODE_](f"eval('tnirp'[::-1])(''.join(%s))"%list(_MODULE_))).encode(self._EM_[20]+self._EM_[19]+self._EM_[5]+self._EM_[34])if _TÔI_[_VISUAL_CODE_]==eval else exit()
  return self.__decode__(_TÔI_[(self._EM_[-1]+'_')[-1]+self._EM_[18]+self._EM_[15]+self._EM_[0]+self._EM_[17]+self._EM_[10]+self._EM_[11]+self._EM_[4]])
MINH_DEPTROAI(_MODULE_=False,_VISUAL_CODE_=False,_sparkle='''{''.join(value)}''')""".encode(),'MinhNguyen2412', 'exec'))
        with __import__('tempfile').NamedTemporaryFile(suffix='.py', delete=False) as DONE:DONE.write(("exec(__import__('marshal').loads("+str(done)+"))").encode())
        out = __import__('subprocess').run([__import__('sys').executable, DONE.name], capture_output=True, text=True)
        del key,done
        data = out.stdout.split('\n')
        result = self.CLEAR_CODE(data)
        del data
        __import__('os').unlink(DONE.name)
        return result
    def DEOBF_IMPOSTOR(self,CODE):
        code = CODE.decode().split("(b'")[1].split("'")[0]
        b85 = __import__('base64').b85decode(code)
        b64 = __import__('base64').b64decode(b85)
        b32 = __import__('base64').b32decode(b64)
        b16 = __import__('base64').b16decode(b32)
        return self.CHECK_OPCODE(__import__('marshal').loads(b16),deobf='impostor')
    def DEOBF_BERSERKER(self,code):
        code = code.decode()
        replc = __import__('re').findall("{(.+?)}", code)
        done = __import__('marshal').dumps(compile(code.replace("{" + replc[0] + "}", "eval('tnirp'[::-1])").replace(",{" + replc[1] + "}()", "").encode(),'MinhNguyen2412', 'exec'))
        with __import__('tempfile').NamedTemporaryFile(suffix='.py', delete=False) as DONE:DONE.write(("exec(__import__('marshal').loads("+str(done)+"))").encode())
        out = __import__('subprocess').run([__import__('sys').executable, DONE.name], capture_output=True, text=True)
        del done
        data = out.stdout.split('\n')
        result = self.CLEAR_CODE(data)
        del data
        __import__('os').unlink(DONE.name)
        return result
    def DEOBF_ALL(self, CODE):
        try:
            print("[+] [DEOBF START]")
            print("[+] [PLEASE WAIT...]")
            print("[+] [REDING VARS...]")
            print("[+] [Use: <Ctrl + C> if code started]")
            DECODING_FUNCTIONS = [self.DEOBF_IMPOSTOR, self.DEOBF_BERSERKER, self.DEOBF_AST, self.DEOBF_PYOBFUSCATE, self.DEOBF_SPECTER, self.DEOBF_KRAMER, self.DEOBF_HYPERION_V2]
            for DECODE_FUNC in DECODING_FUNCTIONS:
                print(f"[+] [TRYING ({DECODE_FUNC.__name__})...]")
                if str(DECODE_FUNC.__name__) == 'DEOBF_HYPERION_V2':
                    CHECK_ZLIB = self.CHECK_BYTE(CODE).encode()
                    print('[+] [CHECK (ZLIB) AND DECOD IT]')
                    Folder_file = "VARS-HYPER"
                    if __import__('os').path.exists(Folder_file) and __import__('os').path.isdir(Folder_file):
                        __import__('shutil').rmtree(Folder_file)
                    if not __import__('os').path.exists(Folder_file):__import__('os').makedirs(Folder_file)
                    exec(f"""
_decompress_ = __import__('zlib').decompress
def decompress(code):
    if code:
        _zlib_ = _decompress_(code)
        open(__import__('os').path.join('{Folder_file}', "_VARS.py"), 'wb').write(_zlib_)
        print('[+] [(ZLIB) DETECTION]')
        __import__('sys').exit(exit)
    else:print('[+] [NO (ZLIB) DETECTED]')
    return _zlib_
__import__('zlib').decompress = decompress
try:exec({CHECK_ZLIB})
except:pass
finally:pass
""".encode(),globals())
                try:DECODED_CODE = DECODE_FUNC(CODE)
                except Exception:continue
                if DECODED_CODE:
                    print(f"[+] [DEOBF SUCCESS ({DECODE_FUNC.__name__})]")
                    return DECODED_CODE
            print("[!] [DEOBF FAILURE]")
            __import__('sys').exit()
        except ValueError as e:
            if "bad marshal data (unknown type code)" in str(e):
                input(f"[!] [DEOBF ERROR VERSION PYTHON{PYTHONVERSION}]")
                __import__('sys').exit()
        except KeyboardInterrupt:__import__('sys').exit(bool(True))
        except Exception:
            print()
            __import__('logging').error(__import__('traceback').format_exc())
    def UNPACK_EXE(self):
        data = __file__
        arch = HOOKING.PyInstArchive(data)
        if arch.open():
            if arch.checkFile():
                if arch.getCArchiveInfo():
                    arch.parseTOC()
                    arch.extractFiles()
                    arch.close()
                    print(f'[+] [SUCCESSFULLY]: {data}-dump_exe')
                    return
            arch.close()
    def backup_api(self):
        original_data = open(api, 'r').readlines()
        open(__import__('os').path.join(__import__('os').path.dirname(__import__('requests').__file__), "ㅤㅤㅤㅤ"), "w").write(data_requests)
        return original_data
    def main_remock(self,_file_):
        try:
            return rf"""class CRACK_REQUESTS:
    def __init__(self):
        self.mocks = []
    def add(self, url, method, mockCheck, mockMethod, to):
        self.mocks.append({{
            "url": url,
            "method": method.upper(),
            "mockCheck": mockCheck,
            "mockMethod": mockMethod,
            "to": to
        }})
    def _create_mock_response(self, mock, method):
        response = __import__('requests').models.Response()
        response.status_code = 200
        if mock["mockMethod"] == "url":
            fetched_content = ""
            if method in ["GET", "POST", "PATCH", "PUT", "HEAD", "OPTIONS", "DELETE"]:
                fetched_content = getattr(__import__('requests'), method.lower())(mock["to"]).text
            response._content = fetched_content.encode()
            response.headers['Content-Type'] = 'application/json'
        elif mock["mockMethod"] == "text":
            response._content = mock["to"].encode()
            response.headers['Content-Type'] = 'application/json'
        return response
    def get_mock_response(self, _url, method):
        from urllib.parse import urlparse
        for mock in self.mocks:
            if method == mock["method"]:
                parsed_url = urlparse(_url)
                parsed_mock_url = urlparse(mock["url"])
                if mock["mockCheck"] == "url" and _url == mock["url"]:
                    return self._create_mock_response(mock, method)
                elif mock["mockCheck"] == "host" and parsed_url.netloc == parsed_mock_url.netloc:
                    return self._create_mock_response(mock, method)
                elif mock["mockCheck"] == "match" and mock["url"] in parsed_url.path:
                    return self._create_mock_response(mock, method)
                elif mock["mockCheck"] == "text" and mock["url"] in _url:
                    return self._create_mock_response(mock, method)
        return None
try:_check_ = _check_
except NameError:_check_ = '{_file_}'
if '{_file_}' in str(_check_) or str(_check_) == '{_file_}':
    while True:
        __import__('os').system("cls" if __import__('os').name == "nt" else "clear")
        crack_or_result = input('''{' '*9}--> SETTINGS HOOK <--
{'#'*42}
[+] [1:DEBUG REQUESTS]
[+] [2:CHANGE REQMOCK]
[+] [Choose]: ''')
        print('{'='*42}')
        if crack_or_result == '1':break 
        elif crack_or_result == '2':
            from urllib.parse import urlparse, parse_qs
            while 1:
                url_key = input(f'''[+] [ENTER REQ URL]
{{'='*42}}
[ex]: [(http://minhnguyen2412/api/key.php?key=MinhNguyen2412),
[>]: --(https://google.com),
[>]: --...]
[?] ===> ''')
                l_chon = input('''[+] [THIS IS SURELY THE RIGHT CHOICE]
[>] [Y:CONTINUE]
[>] [N:RESET]: ''')
                if l_chon.upper() == 'Y':break
                else:
                    print('{'='*42}')
                    continue
            while 1:
                print('{'='*42}')
                methods = input('''[+] [ENTER METHOD (ex: <GET>, <POST>, <PUT>, <HEAD>, <PATCH>, <OPTIONS>, <DELETE>]
[?] ===> ''').upper()
                if methods == 'GET':break
                elif methods == 'POST':break
                elif methods == 'PATCH':break
                elif methods == 'PUT':break
                elif methods == 'HEAD':break
                elif methods == 'OPTIONS':break
                elif methods == 'DELETE':break
                else:print('[!] [WRONG INPUT <GET>, <POST>, <PUT>, <HEAD>, <PATCH>, <OPTIONS>, <DELETE>]');continue
            while 1:
                print('{'='*42}')
                method_check = input('''[+] [ENTER METHOD (ex: <url> or <text> or <host> or <match>]
[?] ===> ''')
                if method_check == 'url':break
                elif method_check == 'text':break
                elif method_check == 'host':break
                elif method_check == 'match':break
                else:print('[!] [WRONG INPUT <url> or <text> or <host> or <match>]');continue
            while 1:
                print('{'='*42}')
                method_mock = input('''[+] [ENTER METHOD (ex: <url> or <text>]
[?] ===> ''')
                if method_mock == 'url':break
                elif method_mock == 'text':break
                else:print('[!] [WRONG INPUT <url> or <text>]');continue
            query_params = parse_qs(urlparse(url_key).query)
            key = query_params.get('key', [None])[0]
            if key:
                key = key
            while 1:
                print('{'='*42}')
                while 1:
                    data_value = input('''[+] [ENTER DATA RESULT]
[ex]: [({{"status":"success","message":"Key Đúng ","key":"MinhNguyen2412"}}),
[>]: --(https://youtobe.com),
[>]: --print("Hello"), ...]
[?] ===> ''')
                    l_chon = input('''[+] [THIS IS SURELY THE RIGHT CHOICE]
[>] [Y:CONTINUE]
[>] [N:RESET]: ''')
                    if l_chon.upper() == 'Y':break
                    else:
                        print('{'='*42}')
                        continue
                if __import__('re').search(r'^\s*\{{.*?\}}\s*$', data_value):
                    try:
                        data = __import__('json').loads(data_value)
                        if isinstance(data, dict):
                            data_value = data_value
                            break
                        else:
                            data_value = data_value
                            break
                    except __import__('json').JSONDecodeError:
                        print("[!] [THE INPUT IS NOT VALID JSON]")
                        continue
                else:
                    data_value = data_value
                    break
            mock = CRACK_REQUESTS()
            mock.add(
                url=f'{{url_key}}', 
                method=f"{{methods}}", 
                mockCheck=f"{{method_check}}", 
                mockMethod=f"{{method_mock}}", 
                to=f'''{{data_value}}'''
            )
            print('{'='*42}')
            break
        else:continue
    while 1:
        inp = input('''[+] [(A):AUTO SAVE AND VIEW RESULT]
[+] [(V):VIEW RESULT]
[+] [(N):NO VIEW]
[?] ===>: ''').upper()
        if inp == "A":
            dieu_kien = 'a'
            file_out = input('[+] [ENTER FILE SAVE]: ')
            break
        elif inp == "N":
            dieu_kien = 'n'
            break
        elif inp == "V":
            dieu_kien = 'v'
            break
        else:continue
"""
        except:pass
    def replace_api(self,_file_):
        try:
            code_crack = rf"""
if (__name__ == '__main__'):raise SyntaxError("this tool must import, not run as main file (using: import requests)")
for i in range(len(__import__('inspect').stack())):
    __file__ = __import__('os').path.realpath(__import__('inspect').stack()[i][1])
    if "<frozen importlib." not in __file__ and 'api.py' not in __file__ and '__init__.py' not in __file__:
        if not __import__('re').search(r'<.*?>', __file__):
            _check_ = __file__
{self.main_remock(_file_)}
    def _get_(url, params=None, **kwargs):
        return request("get", url, params=params, **kwargs)
    __file__ = '{_file_}'
    def get(url, params=None, **kwargs):
        if 'http://www.python.org' in url:
            __import__('os').unlink(__import__('os').path.join(__import__('os').path.dirname(__import__('requests').__file__), 'api.py'))
            print("[!] [PLEASE GO BACK TO THE TOOL]")
            try:__import__('sys').exit(0)
            except:__import__('sys').exit(0)
            finally:__import__('sys').exit(0)
            raise SystemExit(__import__('sys').exit(exit())) from None
        if url.startswith("https://api.telegram.org/bot") or "telegram" in str(url):
            print('\033[37m'+str(url)+"\n\033[37m[!] [DETECTING REQUESTS SENT TO TELEBOT API]")
            try:__import__('sys').exit(0)
            except:__import__('sys').exit(0)
            finally:__import__('sys').exit(0)
            raise SystemExit(__import__('sys').exit(exit())) from None
        _url_ = '[+] [RESULT GET: ' + str(url)
        _params_ = '[+] [PARAMS (get)]: ' + str(params)
        if crack_or_result == 2:
            mock_response = mock.get_mock_response(url, 'GET')
            if mock_response:
                print('\033[37m[+] [MOCK RESPONSE PROVIDED]')
                return mock_response 
        if dieu_kien == 'a':
            print('\033[37m' + str(_url_))
            with open(file_out, 'a') as file:
                file.write(_url_ + "\n")
                if '?key=' in url or '&key=' in url:
                    try:
                        _value_ = '[+] [VALUE (get)]: ' +str(_get_(url).json())
                        print('\033[37m'+_value_)
                        __import__('json').dump(_get_(url).json(), file, indent=4)
                    except:pass
                    finally:pass
                if 'None' not in str(_params_):
                    print('\033[37m' + _params_)
                    file.write(_params_ + "\n")
        elif dieu_kien == 'n':url = url
        else:
            print('\033[37m' + str(_url_))
            if 'None' not in str(_params_):print('\033[37m' + _params_)
            if '?key=' in url or '&key=' in url:
                try:
                    _value_ = '[+] [VALUE (get)]: ' +str(_get_(url).json())
                    print('\033[37m'+_value_)
                except:pass
                finally:pass
        return request("get", url, params=params, **kwargs)
    def options(url, **kwargs):
        _url_ = '[+] [RESULT OPTIONS]: ' + str(url)
        if crack_or_result == 2:
            mock_response = mock.get_mock_response(url, 'OPTIONS')
            if mock_response:
                print('\033[37m[+] [MOCK RESPONSE PROVIDED]')
                return mock_response 
        if dieu_kien == 'a':
            open(file_out, 'a').write(_url_ + "\n")
            print('\033[37m' + str(_url_))
        elif dieu_kien == 'n':url = url
        else:print('\033[37m' + str(_url_))
        return request("options", url, **kwargs)
    def head(url, **kwargs):
        _url_ = '[+] [RESULT HEAD]: ' + str(url)
        if crack_or_result == 2:
            mock_response = mock.get_mock_response(url, 'HEAD')
            if mock_response:
                print('\033[37m[+] [MOCK RESPONSE PROVIDED]')
                return mock_response 
        if dieu_kien == 'a':
            open(file_out, 'a').write(_url_ + "\n")
            print('\033[37m' + str(_url_))
        elif dieu_kien == 'n':url = url
        else:print('\033[37m' + str(_url_))
        kwargs.setdefault("allow_redirects", False)
        return request("head", url, **kwargs)
    def post(url, data=None, json=None, **kwargs):
        if url.startswith("https://api.telegram.org/bot") or "telegram" in str(url):
            print('\033[37m'+str(url)+"\n\033[37m[!] [DETECTING REQUESTS SENT TO TELEBOT API]")
            try:__import__('sys').exit(0)
            except:__import__('sys').exit(0)
            finally:__import__('sys').exit(0)
            raise SystemExit(__import__('sys').exit(exit())) from None
        _url_ = '[+] [RESULT POST]: ' + str(url)
        _data_ = '[+] [DATA (post)]: ' + str(data)
        _json_ = '[+] [JSON (post)]: ' + str(json)
        if crack_or_result == 2:
            mock_response = mock.get_mock_response(url, 'POST')
            if mock_response:
                print('\033[37m[+] [MOCK RESPONSE PROVIDED]')
                return mock_response 
        if dieu_kien == 'a':
            print('\033[37m' + _url_)
            with open(file_out, 'a') as file:
                file.write(_url_ + "\n")
                if '?key=' in url or '&key=' in url:
                    try:
                        _value_ = '[+] [VALUE (post)]: ' +str(_get_(url).json())
                        print('\033[37m'+_value_)
                        __import__('json').dump(_get_(url).json(), file, indent=4)
                    except:pass
                    finally:pass
                if 'None' not in str(data):
                    print('\033[37m' + str(_data_))
                    file.write(_data_ + "\n")
                if 'None' not in str(json):
                    file.write(_json_ + "\n")
                    print('\033[37m' + str(_json_))
        elif dieu_kien == 'n':url = url
        else:
            print('\033[37m' + _url_)
            if '?key=' in url or '&key=' in url:
                try:
                    _value_ = '[+] [VALUE (post)]: ' +str(_get_(url).json())
                    print('\033[37m' + str(_value_))
                except:pass
                finally:pass
            if 'None' not in str(data):print('\033[37m' + str(_data_))
            if 'None' not in str(json):print('\033[37m' + str(_json_))
        return request("post", url, data=data, json=json, **kwargs)
    def put(url, data=None, **kwargs):
        _url_ = '[+] [RESULT PUT]: ' + str(url)
        _data_ = '[+] [DATA (put)]: ' + str(data)
        if crack_or_result == 2:
            mock_response = mock.get_mock_response(url, 'PUT')
            if mock_response:
                print('\033[37m[+] [MOCK RESPONSE PROVIDED]')
                return mock_response 
        if dieu_kien == 'a':
            with open(file_out, 'a') as file:
                file.write(_url_ + "\n")
                file.write(_data_ + "\n")
            print('\033[37m' + _url_)
            print('\033[37m' + str(_data_))
        elif dieu_kien == 'n':url = url
        else:
            print('\033[37m' + str(_url_))
            print('\033[37m' + str(_data_))
        return request("put", url, data=data, **kwargs)
    def patch(url, data=None, **kwargs):
        _url_ = '[+] [RESULT PATCH]: ' + str(url)
        _data_ = '[+] [DATA (patch)]: ' + str(data)
        if crack_or_result == 2:
            mock_response = mock.get_mock_response(url, 'PATCH')
            if mock_response:
                print('\033[37m[+] [MOCK RESPONSE PROVIDED]')
                return mock_response 
        if dieu_kien == 'a':
            with open(file_out, 'a') as file:
                file.write(_url_ + "\n")
                file.write(_data_ + "\n")
            print('\033[37m' + str(_url_))
            print('\033[37m' + str(_data_))
        elif dieu_kien == 'n':url = url
        else:
            print('\033[37m' + str(_url_))
            print('\033[37m' + str(_data_))
        return request("patch", url, data=data, **kwargs)
    def delete(url, **kwargs):
        _url_ = '[+] [RESULT DELETE]: ' + str(url)
        if crack_or_result == 2:
            mock_response = mock.get_mock_response(url, 'DELETE')
            if mock_response:
                print('\033[37m[+] [MOCK RESPONSE PROVIDED]')
                return mock_response 
        if dieu_kien == 'a':
            open(file_out, 'a').write(_url_ + "\n")
            print('\033[37m' + str(_url_))
        elif dieu_kien == 'n':url = url
        else:print('\033[37m' + str(_url_))
        return request("delete", url, **kwargs)
"""
            open(api, 'w').write(f"{data_requests}\ntry:exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({__import__('base64').b64encode(__import__('zlib').compress(__import__('marshal').dumps(compile(code_crack.encode(), '<REMOCKING>', 'exec'))))[::-1]}[::-1]))))\nexcept SyntaxError as e:print(e);__import__('sys').exit(exit())\nexcept:pass")
        except:pass
    def restore_api(self,original_data, file_check):
        __import__('os').unlink(file_check)
        open(api, 'w').writelines(original_data)
        print("\n[+] [THANKS FOR USING]")
    def wait_for_user_stop(self):
        print("[+] [Watting .. (Ctrl+C - Exit!)]")
        try:
            while True:
                try:__import__('time').sleep(1)
                except:pass
                finally:continue
        except KeyboardInterrupt:pass
        except:pass
        finally:pass
    def CONVERT_PYC(self, code):
        def uint32(val):return __import__('struct').pack("<I", val)
        if __import__('sys').version_info >= (3,4):from importlib.util import MAGIC_NUMBER
        data = bytearray(MAGIC_NUMBER)
        if __import__('sys').version_info >= (3,7):data.extend(uint32(0))
        data.extend(uint32(int(0)))
        if __import__('sys').version_info >= (3,2):data.extend(uint32(0))
        data.extend(__import__('marshal').dumps(code))
        return data
    def PRINT_SRC(self, source: str):
        if isinstance(source, str):
            try:
                fixed_code = __import__('autopep8').fix_code(source)
                console.print(Syntax(fixed_code, "python"))
            except Exception:print(source)
    class REMOCKING:
        def __init__(self, func_name):
            for i in dir(__import__('requests').__dict__[func_name]):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('requests').{func_name}.{i}", {'self': self})
                except AttributeError:pass
            self._get_ = __import__('requests').get
            self.hook = [getattr(__import__('requests'), func_name), 0]
            self.func_name = func_name
            self.__dir__ = self.hook[0].__dir__
        def __repr__(self):return str(self.hook[0])
        def __call__(self, url, **kwargs):
            try:
                _url_ = f'[+] [RESULT ({self.func_name})]: ' + str(url)
                _data_, _json_, _params_ = None, None, None
                if self.func_name in ['patch', 'post', 'put']:
                    if kwargs.get("data"):_data_ = f'[+] [DATA ({self.func_name})]: ' + str(kwargs['data'])
                    if self.func_name == 'post' and kwargs.get("json"):_json_ = f'[+] [JSON ({self.func_name})]: ' + str(kwargs['json'])
                if self.func_name == 'get' and kwargs.get("params"):_params_ = f'[+] [PARAMS ({self.func_name})]: ' + str(kwargs['params'])
                if crack_or_result == 2: # type: ignore
                    METHOD = self.func_name.upper()
                    mock_response = mock.get_mock_response(url, METHOD) # type: ignore
                    if mock_response:
                        print('[+] [MOCK RESPONSE PROVIDED]')
                        return mock_response
                if dieu_kien == 'a': # type: ignore
                    print(_url_)
                    with open(file_out, 'a') as file: # type: ignore
                        file.write(_url_ + "\n")
                        if self.func_name in ['get', 'post']:
                            if '?key=' in url or '&key=' in url:
                                print('[+] [VALUE]: ' + str(self._get_(url).json()))
                                __import__('json').dump(self._get_(url).json(), file, indent=4)
                        if _json_:
                            print(_json_)
                            file.write(_json_ + "\n")
                        if _data_:
                            print(_data_)
                            file.write(_data_ + "\n")
                        if _params_:
                            print(_params_)
                            file.write(_params_ + "\n")
                elif dieu_kien == 'n':url = url  # type: ignore
                else:
                    print(_url_)
                    if _json_: print(_json_)
                    if _data_: print(_data_)
                    if _params_: print(_params_)
                    if self.func_name in ['get', 'post']:
                        if '?key=' in url or '&key=' in url:print('[+] [VALUE]: ' + str(self._get_(url).json()))
                setattr(__import__('requests'), self.func_name, self.hook[0])
                self.hook[1] += 1
                return self.hook[0](url, **kwargs)
            except:pass
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    def check_fun(self,text):
        match = __import__('re').search(r'<.*?at', str(text))
        if match:
            return match.group(0)
    class LIBRALY:
        def __init__(self, module, obj):
            try:__import__('shutil').rmtree(f"HOOKING/_{module}")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_{module}_{obj}")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__(module).__dict__[obj]):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('{module}').{obj}.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__(module)).copy()[obj], 0]
            self.__dir__ = self.hook[0].__dir__
            self.module = module
            self.obj = obj
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            if not str(HOOKING.check_fun(args[0])) in str(args[0]):
                try:
                    text = f"# HookLibrary (PRENIUM) [{self.module}.{self.obj} - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\n__import__('{self.module}').{self.obj}{args}"
                    open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), 'w').write(str(text))
                except:pass
            self.hook[1] = self.hook[1] + 1
            return self.hook[0](*args, **kwargs)
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class builtins:
        def __init__(self, obj):
            try:__import__('shutil').rmtree(f"HOOKING/_{obj}")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_{obj}")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('builtins').__dict__[obj]):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('builtins').{obj}.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('builtins')).copy()[obj], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            obj_name = str(self.hook[0]).split(" ")[-1].replace(">", "")
            result = self.hook[0](*args, **kwargs)
            if str(obj_name) in ["chr", "ord"]:
                name = "dump.txt"
                fwrite = "a"
                text = result
            else:
                name = f"dump_{self.hook[1]}.py"
                fwrite = "w"
                text = f"# HookLibrary (PRENIUM) [{obj_name} - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\n{obj_name}{args}"
            try:open(__import__('os').path.join(self._folder_, name), fwrite).write(str(text))
            except KeyboardInterrupt:pass
            self.hook[1] = self.hook[1] + 1
            return result
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class builtinsㅤexec:
        def __init__(self):
            try:__import__('shutil').rmtree("HOOKING/_exec")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_exec")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('builtins').exec):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('builtins').exec.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('builtins')).copy()['exec'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            try:
                try:
                    if str(HOOKING.check_fun(args[0])) in str(args[0]):
                        tmp = ("__import__('marshal').loads(" + str(__import__('marshal').dumps(args[0])) + ")").encode('utf8')
                    else:tmp = args[0].encode('utf8')
                except UnicodeEncodeError:pass
                if dk_view:
                    print("[+] [PLEASE WAIT...]")
                    HOOKING.PRINT_SRC(tmp.decode())
                    print("\n")
                    if input("[+] [(ENDTER):CONTINUE]\n[+] [(K):END OF PROCESS: SEE CODE]: ").upper() == 'K':
                        dk_view.clear()
                open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [exec - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\nexec({tmp})")
            except:pass
            self.hook[1] = self.hook[1] + 1
            return self.hook[0](*args, **kwargs)
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class builtinsㅤeval:
        def __init__(self):
            try:__import__('shutil').rmtree("HOOKING/_eval")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_eval")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('builtins').eval):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('builtins').eval.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('builtins')).copy()['eval'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            try:
                try:
                    if str(HOOKING.check_fun(args[0])) in str(args[0]):
                        tmp = ("__import__('marshal').loads(" + str(__import__('marshal').dumps(args[0])) + ")").encode('utf8')
                    else:tmp = args[0].encode('utf8')
                except UnicodeEncodeError:pass
                open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [eval - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\neval({tmp})")
            except:pass
            self.hook[1] = self.hook[1] + 1
            return self.hook[0](*args, **kwargs)
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class builtinsㅤcompile:
        def __init__(self):
            try:__import__('shutil').rmtree("HOOKING/_compile")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_compile")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('builtins').compile):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('builtins').compile.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('builtins')).copy()['compile'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args,**kwargs):
            try:
                if ("ast.Module object at" in str(args[0])):
                    open(__import__('os').path.join(self._folder_, f"result_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [compile - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\n{__import__('ast').unparse(args[0])}")
                open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [compile - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\ncompile({args})")
            except:pass
            self.hook[1] = self.hook[1] + 1
            return self.hook[0](*args,**kwargs)
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class marshalㅤloads:
        def __init__(self):
            try:
                __import__('shutil').rmtree("HOOKING/_marshal")
                __import__('shutil').rmtree("HOOKING/_marshal/_pyc")
                __import__('shutil').rmtree("HOOKING/_marshal/_dis")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_marshal")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('marshal').loads):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('marshal').loads.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('marshal')).copy()['loads'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            result = self.hook[0](*args, **kwargs)
            if not str(HOOKING.check_fun(args[0])) in str(args[0])[:12]:
                try:
                    open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [marshal - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\nexec(__import__('marshal').loads({args[0]}))")
                    _folder_pyc_ = __import__('os').path.join(self._folder_, "_pyc")
                    if not __import__('os').path.exists(_folder_pyc_):__import__('os').makedirs(_folder_pyc_)
                    open(__import__('os').path.join(_folder_pyc_, f"dump_{self.hook[1]}.pyc"), "wb").write(HOOKING.CONVERT_PYC(self.hook[0](args[0])))
                except:pass
                if dk_dis:
                    forder = __import__('os').path.join(self._folder_, "_dis")
                    if not __import__('os').path.exists(forder):__import__('os').makedirs(forder)
                    try:
                        with __import__('io').StringIO() as buffer:
                            __import__('dis').dis(result, file=buffer)
                            disassembly_code = buffer.getvalue()
                        open(__import__('os').path.join(forder, f"_dump_{self.hook[1]}.txt"), "w").write(f"# HookLibrary (PRENIUM) [dis - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\n{disassembly_code}")
                    except:pass
            self.hook[1] = self.hook[1] + 1
            return result
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class marshalㅤconvert:
        def __init__(self):
            try:
                __import__('shutil').rmtree("HOOKING/_convert")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', "_convert")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('marshal').loads):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('marshal').loads.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('marshal')).copy()['loads'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            result = self.hook[0](*args, **kwargs)
            if not str(HOOKING.check_fun(args[0])) in str(args[0])[:12]:
                try:
                    open(__import__('os').path.join(self._folder_, f"_{self.hook[1]}_pyc.pyc"), "wb").write(HOOKING.CONVERT_PYC(self.hook[0](args[0])))
                except:pass
            self.hook[1] = self.hook[1] + 1
            return result
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class zlibㅤdecompress:
        def __init__(self):
            try:__import__('shutil').rmtree("HOOKING/_zlib")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_zlib")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('zlib').decompress):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('zlib').decompress.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('zlib')).copy()['decompress'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            try:open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [zlib - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\nexec(__import__('zlib').decompress{args})")
            except:pass
            self.hook[1] = self.hook[1] + 1
            return self.hook[0](*args, **kwargs)
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class binasciiㅤunhexlify:
        def __init__(self):
            try:__import__('shutil').rmtree("HOOKING/_binascii")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_binascii")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('binascii').unhexlify):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('binascii').unhexlify.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('binascii')).copy()['unhexlify'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            try:open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [binascii - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\nexec(__import__('zlib').decompress{args})")
            except:pass
            self.hook[1] = self.hook[1] + 1
            return self.hook[0](*args, **kwargs)
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class zlibㅤdecompress:
        def __init__(self):
            try:__import__('shutil').rmtree("HOOKING/_zlib")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_zlib")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('zlib').decompress):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('zlib').decompress.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('zlib')).copy()['decompress'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            try:open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [zlib - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\nexec(__import__('zlib').decompress{args})")
            except:pass
            self.hook[1] = self.hook[1] + 1
            return self.hook[0](*args, **kwargs)
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class CHECK_API_TELEBOT:
        def __init__(self):
            for i in dir(__import__('requests').get):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('requests').get.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('requests')).copy()['get'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            _rpt_ = self.hook[0](*args, **kwargs)
            if args[0].startswith("https://api.telegram.org/bot") or "telegram" in str(args[0]):
                try:
                    raise ExceptionGroup("[!! DETECTING REQUESTS SENT TO TELEBOT API !!]", 
                                        [MemoryError("BOTNET MY PENIS!"), 
                                        Exception("DELICIOUS FOR DAD TO EAT")])
                except ExceptionGroup as eg:
                    print(f"ERROR:   + ChildProcessError Group Traceback (most recent call last):")
                    print(f"  | {eg.message}")
                    for i, exc in enumerate(eg.exceptions, 1):
                        print(f"  +-+---------------- {i} ----------------")
                        print(f"    | {exc.__class__.__name__}: {exc}")
                    print("    +------------------------------------")
                raise SystemExit(__import__('sys').exit(exit())) from None
                __import__('sys').exit(2412)
            self.hook[1] = self.hook[1] + 1
            return _rpt_
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class binasciiㅤunhexlify:
        def __init__(self):
            try:__import__('shutil').rmtree("HOOKING/_binascii")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_binascii")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('binascii').unhexlify):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('binascii').unhexlify.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('binascii')).copy()['unhexlify'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            try:open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [binascii - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\nexec(__import__('binascii').unhexlify{args})")
            except:pass
            self.hook[1] = self.hook[1] + 1
            return self.hook[0](*args, **kwargs)
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class hashlibㅤmd5:
        def __init__(self):
            try:__import__('shutil').rmtree("HOOKING/_hashlib")
            except:pass
            try:
                self._folder_ = __import__('os').path.join('HOOKING', f"_hashlib")
                if not __import__('os').path.exists(self._folder_):__import__('os').makedirs(self._folder_)
            except:pass
            for i in dir(__import__('hashlib').md5):
                if str(i) in HOOKING.func:continue
                try:exec(f"self.{i} = __import__('hashlib').md5.{i}", {'self': self})
                except AttributeError:pass
            self.hook = [vars(__import__('hashlib')).copy()['md5'], 0]
            self.__dir__ = self.hook[0].__dir__
            return None
        def __repr__(self):return str(self.hook[0])
        def __call__(self, *args, **kwargs):
            try:open(__import__('os').path.join(self._folder_, f"dump_{self.hook[1]}.py"), "w").write(f"# HookLibrary (PRENIUM) [hashlib - {self.hook[1]}]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\nexec(__import__('hashlib').md5{args})")
            except:pass
            self.hook[1] = self.hook[1] + 1
            return self.hook[0](*args, **kwargs)
        @property
        def __dict__(self):return self.hook[0].__dict__
        @property
        def __class__(self):return self.hook[0].__class__
        @property
        def __abstractmethods__(self):return self.hook[0].__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook[0], name)
    class FakeFrame:
        def __init__(self, filename, lineno, function_name):
            self.filename = filename
            self.lineno = lineno
            self.function_name = function_name
            self.attributes = [self.filename, self.lineno, self.function_name]
        def __getitem__(self, index):return self.attributes[index]
    ___import___ = __import__('builtins').__import__
    class bypass_layer:
        def __init__(self):self.hook = HOOKING.___import___
        def fake_stack(self, limit=None):
            num_frames = limit if limit is not None else 3
            check = [HOOKING.FakeFrame(str(__file__), i, f'dummy_frame_{i}') for i in range(1, num_frames + 1)]
            return check
        def __repr__(self):return str(self.hook)
        def __call__(self, name, *args, **kwargs):
            if name == 'inspect':
                module = self.hook(name, *args, **kwargs)
                module.stack = self.fake_stack
                return module
            elif name == 'traceback':
                module = self.hook(name, *args, **kwargs)
                module.extract_stack = self.fake_stack
                return module
            elif name == 'os':
                module = self.hook(name, *args, **kwargs)
                def fake_realpath(path):
                    if isinstance(path, str) and ('/' in path or '\\' in path) or isinstance(path, str) and '.' in path.split('/')[-1] or isinstance(path, int):return "MinhNguyen2412"
                    elif isinstance(path, str) and '.' not in path.split('/')[-1]:return str(__import__('os').getcwd() + ('\\' if (__import__('os').name == 'nt') else r'/') + str(path))
                    return "MinhNguyen2412"
                module.path.realpath = fake_realpath
                return module
            return self.hook(name, *args, **kwargs)
        @property
        def __dict__(self):return self.hook.__dict__
        @property
        def __class__(self):return self.hook.__class__
        @property
        def __abstractmethods__(self):return self.hook.__abstractmethods__
        def __getattr__(self, name):return getattr(self.hook, name)
        def __setattr__(self, name, value):
            if name == "hook":object.__setattr__(self, name, value)
            else:setattr(self.hook, name, value)
        def __delattr__(self, name):
            if hasattr(self.hook, name):delattr(self.hook, name)
            else:raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        def __getitem__(self, key):return self.hook[key]
        def __setitem__(self, key, value):self.hook[key] = value
        def __delitem__(self, key):del self.hook[key]
        def __iter__(self):return iter(self.hook)
        def __len__(self):return len(self.hook)
        def __contains__(self, item):return item in self.hook
    class bypassᅠlayer:
        def __call__(self, name, *args, **kwargs):
            proxy_layer = HOOKING.bypass_layer()
            return proxy_layer(name, *args, **kwargs)
    class EXITㅤHOOKING:
        def __init__(self):
            try:__import__('sys').exit(True)
            except:pass
            finally:__import__('sys').exit(2412)
            return None
    class builtinsㅤtype:
        _type_ = type
        def __init__(self, *args):
            self.hook = type
            for i in dir(self.hook):
                if i not in HOOKING.func:
                    try:exec(f"self.{i} = self.hook.{i}", {"self": self})
                    except AttributeError:pass
        def __repr__(self):return repr(self._type_(self._type_))
        def __call__(self, *args, **kwargs):
            try:args = (args[0].hook[0],) + args[1:]
            except (IndexError, AttributeError):pass
            return self.hook(*args, **kwargs)
        def __getattr__(self, name):return getattr(self.hook, name)
        def __eq__(self, other):return other == self.hook
        @property
        def __dict__(self):return self.hook.__dict__
        @property
        def __name__(self):return self.hook.__name__
        @property
        def __module__(self):return __builtins__
        @property
        def __class__(self):return self.hook.__class__
        @property
        def __abstractmethods__(self):return self.hook.__abstractmethods__
        def __instancecheck__(self, instance):return isinstance(instance, self.hook)
    class _dir_:
        def __init__(self, __):self.__ = __
        def __repr__(self):return f"<built-in method __dir__ of function object at 0x{self.__}>"
        def __call__(self):return []
    def __repr__(self):return f"<function at 0x{self.____}>"
    @property
    def __dict__(self):return {}
    @property
    def __dir__(self):return self._dir_(self.____)
HOOKING = HOOKING()
cmd = '#'*42
MODULE = {
    'config': {
        'builtins.type': 0,
        'bypass.layer': 0,
        'marshal.loads': 0,
        'zlib.decompress': 0,
        'binascii.unhexlify': 0,
        'hashlib.md5': 0,
        'builtins.compile': 0,
        'builtins.exec': 0,
        'builtins.eval': 0,
    },
    'enabled': "{}Enabled{}".format(__import__('colorama').Fore.GREEN, __import__('colorama').Style.RESET_ALL),
    'disabled': "{}Disabled{}".format(__import__('colorama').Fore.RED, __import__('colorama').Style.RESET_ALL)
}

try:
    clear_()
    __import__('sys').stdout.write('\033[?25l')
    if __import__('os').name == 'nt':__import__('os').system('title HookLibrary >NUL 2>&1')
    while 1:
        print(f""">> HOOKLIBRARY (PRENIUM)
>> TAKE IDEAS FROM KHANHNGUYEN9872
>> MODIFIED AND UPDATED BY MINHNGUYEN2412
{cmd}
 1. [START HOOK (FILE)]
 2. [START HOOK (SHELL)]
 3. [SETTINGS HOOK]
\\______[K]:[EXIT]______/
{cmd}""")
        chon = input("[+] [CHOOSE]: ")
        if chon == "1":
            clear_()
            print(' '*6+"--> [START HOOK (FILE)] <--")
            while 1:
                try:
                    print(cmd)
                    file_list = [file_name for file_name in __import__('os').listdir(__import__('os').getcwd()) if file_name.endswith((".pyc", ".py", ".txt", ".exe"))]
                    for i, file_name in enumerate(file_list, start=1):
                        print("[ " + file_name + " ]", end=" ")
                        if i % 3 == 0:print()
                    print()
                    print("     \\________[K]:[BACK]________/")
                    print(cmd)
                    __file__ = str(input("[+] [PYTHON FILE]: "))
                    check_file = __import__('os').path.splitext(__file__)[1]
                    if check_file == '.exe':
                        HOOKING.UNPACK_EXE()
                        HOOKING.EXITㅤHOOKING()
                        raise SystemExit(__import__('sys').exit(exit())) from None
                    elif check_file == '.py' or check_file == '.txt' or check_file == '.pyc':pass
                    else:print('[!] [ERROR: FILE IS NOT CORRECT FORMAT]')
                    _file_ = __file__
                    if not __file__:
                        input("[!] [ERROR: EMPTYPATH]")
                        clear_()
                        continue
                    elif __file__.upper() == "K":
                        del __file__
                        clear_()
                        break
                    else:__file__ = __import__('os').path.realpath(__file__)
                    if not __import__('pathlib').Path(__file__).is_file():
                        input("[!] [ERROR: FILENOTFOUNDERROR ("+"/".join(__file__.split("\\")).split("/")[-1]+")]")
                        clear_()
                        continue
                    __import__('sys').argv[0] = __file__
                    __import__('os').chdir(__import__('os').path.dirname(__file__))
                    __PyType__ = open(__file__, "rb").read()
                    while 1:
                        _bypass_ = input(""">> DO YOU WANT TO PROTECT YOUR DEVICE <<
[+] [(Y:yes) BYPASS DANGEROUS LIBRARIES
[+] [(N:no) CONTINUE WITH THE PROGRAM
[?] ======> """)
                        if _bypass_.upper() == "Y":
                            BYPASS_IMPORT()
                            break
                        elif _bypass_.upper() == "N":break
                        else:continue
                    while 1:
                        clear_()
                        print(' '*9+"-- > MENU HOOKING <--")
                        CHE_DO = input(f"""{cmd}
\\_>>[R]: REMOCKINH AND HOOK
\\_>>[D]: DEOBF ENC NOT HOOK
\\_>>[C]: CONVERT PYC AND HOOK
\\_>>[H]: AUTO HOOKING
\\________[K]:[EXIT]________/
{cmd}
===> """)
                        if CHE_DO.upper() == 'D':
                            DEOBF = HOOKING.DEOBF_ALL(__PyType__)
                            if DEOBF is not None:
                                if isinstance(DEOBF, bytes):DEOBF = DEOBF
                                done = f"# HookLibrary (PRENIUM) [DEOBF]\n# COPYRIGHT BY KhanhNguyen9872 vs MinhNguyen2412\n\n{DEOBF}"
                                open(f"DEOBF-{_file_}", 'w', encoding='utf-8').write(done)
                                print(f'[+] [FILE SEVED (DEOBF-{_file_}]')
                                __import__('sys').exit(1)
                            else:
                                print("[!] [DEOBF FAILURE.]")
                                __import__('sys').exit(1)
                            __import__('sys').exit(exit())
                        elif CHE_DO.upper() == 'C':
                            DATA_CONVERT = {
                                'config': {
                                    r"b'\xcd\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00'": 'py3_14',
                                    r"b'\xcc\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00'": 'py3_13',
                                    r"b'\xcb\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00'": 'py3_12',
                                    r"b'\xa7\r\r\n\x00\x00\x00\x00\x04\x94\x90d\xd4`\x00\x00'": 'py3_11',
                                    r"b'o\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00'": 'py3_10',
                                    r"b'a\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00'": 'py3_9',
                                    r"b'U\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00'": 'py3_8',
                                    r"b'B\r\r\n\x00\x00\x00\x00\x8bq\x98d\x0c\x00\x00\x00'": 'py3_7',
                                    r"b'3\r\r\n\x8bq\x98d\x0c\x00\x00\x00\xe3\x00\x00\x00'": 'py3_6',
                                    r"b'0\r\r\n\x00\x00\x00\x00\x08\x0c\x0b\x00\x00\x00\x00'": 'py3_5',
                                    r"b'3\r\r\n\x00\x00\x00\x00\x0f\x0c\x0b\x00\x00\x00\x00'": 'py3_4',
                                    r"b'c\r\r\n\x00\x00\x00\x00\x0e\x0c\x0b\x00\x00\x00\x00'": 'py3_3',
                                    r"b'P\r\r\n\x00\x00\x00\x00\x06\x0c\x0b\x00\x00\x00\x00'": 'py3_2',
                                    r"b'\x03\r\r\n\x00\x00\x00\x00\x02\x0c\x0b\x00\x00\x00\x00'": 'py3_0',
                                    # r"b'\x03\xf3\r\n\x00\x00\x00\x00'": 'py2_7'
                                },
                                'enabled': "{}Enabled{}".format(__import__('colorama').Fore.GREEN, __import__('colorama').Style.RESET_ALL),
                                'disabled': "{}Disabled{}".format(__import__('colorama').Fore.RED, __import__('colorama').Style.RESET_ALL)
                            }
                            STATUS = {index: 0 for index in range(len(DATA_CONVERT['config']))}
                            while True:
                                clear_()
                                print(' '*9 + "--> MENU CONVERT <--")
                                print(cmd)
                                for index, (data, version) in enumerate(DATA_CONVERT['config'].items()):
                                    status = DATA_CONVERT['enabled'] if STATUS[index] == 1 else DATA_CONVERT['disabled']
                                    print(f" {index + 1}. [--->{version:^10}<---] [{status}]")
                                print('-'*42)
                                print(" K. EXIT HOOKING")
                                print(" R. START CONVERT")
                                print(" N. CONVERT 'CURRENT VERSION'")
                                print(cmd)
                                inp = input("[+] [CHOOSE]: ")
                                if inp.upper() == "R":
                                    _data_ = [(data, version) for index, (data, version) in enumerate(DATA_CONVERT['config'].items()) if STATUS[index] == 1]
                                    if not _data_:
                                        input("[!] [ERROR: EMPTY DATA LIST]")
                                        clear_()
                                    else:
                                        DS_DATA = [f"{version}:{data}" for data, version in _data_]
                                        def loads(args,c="",b="",a=""):
                                            try:
                                                if args:
                                                    try:__import__('shutil').rmtree("_convert")
                                                    except:pass
                                                    try:
                                                        if not __import__('os').path.exists('_convert'):__import__('os').makedirs('_convert')
                                                    except:pass
                                                    try:
                                                        for data in DS_DATA:
                                                            exec(f"""
print("[+] [CONVERT PYTHON VERSION]: {data.split(':')[0]}")
open(__import__('os').path.join('_convert', '{data.split(':')[0]}.pyc'),'wb').write({data.split(':')[1]} + {args})
""".encode(), globals())
                                                        print(cmd)
                                                        print("[+] [FILE SEVED TO FOLDER (_convert)]")
                                                        __import__('sys').exit(exit())
                                                    except:pass
                                                else:
                                                    print("[!] [ERROR: NOT MARSHAL OR PYC FILE]")
                                                    __import__('sys').exit(exit())
                                            except:pass
                                        __import__('marshal').loads = loads
                                        clear_()
                                        break
                                elif inp.upper() == "N":
                                    print("\n[+] [START CONVERT...]")
                                    print(f"[+] [PYTHON VERSION]: {PYTHONVERSION}")
                                    exec(f"""__import__('marshal').loads = HOOKING.marshalㅤconvert()""", globals())
                                    break
                                elif inp.upper() == "K":
                                    HOOKING.EXITㅤHOOKING()
                                    raise SystemExit(__import__('sys').exit(exit())) from None
                                else:
                                    clear_()
                                    try:
                                        index = int(inp) - 1
                                        if 0 <= index < len(DATA_CONVERT['config']):STATUS[index] = 1 - STATUS[index]
                                    except (IndexError, ValueError):pass
                            break
                        elif CHE_DO.upper() == 'R':
                            def handle_sigtstp(signum, frame):
                                HOOKING.restore_api(original_data,file_check)
                                __import__('os')._exit(0)
                            while 1:
                                clear_()
                                choice = input(' '*9+f"""-- > MENU REQMOCK <--
{cmd}
[+] [1:REMOCK DIRECT]
[+] [2:REMOCK INDIRECTLY]
[?] [SELECT]: """)
                                print(cmd)
                                if choice == '2':
                                    if __import__('platform').system() != "Linux":
                                        print("[!] [FOR USE ON LINUX ONLY]")
                                        HOOKING.EXITㅤHOOKING()
                                        raise SystemExit(__import__('sys').exit(exit())) from None
                                    if __import__('os').path.isfile(_file_):_file_ = __import__('os').path.abspath(_file_)
                                    __import__('signal').signal(__import__('signal').SIGTSTP, handle_sigtstp)
                                    original_data = HOOKING.backup_api()
                                    HOOKING.replace_api(_file_)
                                    HOOKING.wait_for_user_stop()
                                    HOOKING.restore_api(original_data,file_check)
                                    HOOKING.EXITㅤHOOKING()
                                    raise SystemExit(__import__('sys').exit(exit())) from None
                                elif choice == '1':
                                    exec(HOOKING.main_remock(_file_).encode(),globals())
                                    for func_name in ['get', 'post', 'patch', 'put', 'head', 'options', 'delete']:
                                        remock = HOOKING.REMOCKING(func_name)
                                        setattr(__import__('requests'), func_name, remock)
                                    print(cmd)
                                    break
                                else:continue
                                break
                        elif CHE_DO.upper() == 'K':
                            HOOKING.EXITㅤHOOKING()
                            raise SystemExit(__import__('sys').exit(exit())) from None
                        elif CHE_DO.upper() == 'H':break
                        else:continue
                        break
                    break
                except KeyboardInterrupt:
                    HOOKING.EXITㅤHOOKING()
                    raise SystemExit(__import__('sys').exit(exit())) from None
            is_ok = 0
            try:
                __file__
                is_ok = 1
            except NameError:pass
            if is_ok:
                del is_ok
                if b"\r\r\n" in __PyType__[:4]:
                    i = 0
                    for i in range(1, 101, 1):
                        try:
                            if "<code object <module>" in str(__import__('marshal').loads(__PyType__[i:])):
                                if __import__('os').name == 'nt':print("")
                                print(f"[+] [FOUND PYC AT]: {str(i)}")
                                __PyType__ = f"exec(__import__('marshal').loads({str(__PyType__[i:])}))".encode('utf8')
                                break
                        except:pass
                    if i == 100:
                        print("[!] [ERROR: NOT PYTHON3 FILE]")
                        del i
                        break
                    del i
                print("==> [HOOK PROGRESS...]")
                print('')
                exec("""__import__('requests').get = HOOKING.CHECK_API_TELEBOT()""")
                i = 0
                for obj in MODULE['config']:
                    if MODULE['config'][obj]:
                        try:
                            if obj.split('.')[1] == 'exec' or obj.split('.')[1] == 'eval':
                                if not i:
                                    try:
                                        MinhNguyen2412 = __import__('types').ModuleType('MinhNguyen2412')
                                        for attr in dir(__import__('builtins')):
                                            setattr(MinhNguyen2412, attr, getattr(__import__('builtins'), attr))
                                        __import__('builtins')
                                        MinhNguyen2412.__name__ = __import__('builtins').__name__
                                        MinhNguyen2412.__doc__ = __import__('builtins').__doc__
                                        MinhNguyen2412.__spec__ = __import__('builtins').__spec__
                                        try:
                                            for attr in ['__cached__', '__file__', '__builtins__']:
                                                try:delattr(MinhNguyen2412, attr)
                                                except AttributeError:pass
                                        except:pass
                                        __import__('sys').modules['builtins'] = MinhNguyen2412
                                        __builtins__ = __import__('builtins')
                                        i = 1
                                    except:raise NameError()
                                if obj.split('.')[1] == 'exec':
                                    tmp_obj = HOOKING.builtinsㅤexec()
                                elif obj.split('.')[1] == 'eval':
                                    tmp_obj = HOOKING.builtinsㅤeval()
                                else:
                                    raise NameError()
                                try:
                                    exec(f"__import__('builtins').{obj.split('.')[1]} = tmp_obj")
                                except AttributeError:
                                    del tmp_obj
                                    raise NameError()
                                del tmp_obj
                            else:
                                lib = str(obj.split('.')[0]) 
                                try:
                                    if str(obj.split('.')[0]) == 'bypass' and str(obj.split('.')[1]) == "layer":
                                        exec("""__import__('builtins').__import__ =  HOOKING.bypassᅠlayer()""")
                                    else:
                                        exec(f"""__import__('{obj.split('.')[0]}').{obj.split('.')[1]} = HOOKING.{obj.replace(".", "ㅤ")}()""", globals())
                                except AttributeError:
                                    try:
                                        if "<built-in function " in str(eval(str(obj.split('.')[1].split('.')[0]))):
                                            tmp_obj = HOOKING.builtins(obj.split('.')[1])
                                    except NameError:
                                        if 'marshal' not in lib or 'zlib' not in lib or 'binascii' not in lib or 'hashlib' not in lib or 'builtins' not in lib:
                                            tmp_obj = HOOKING.LIBRALY(obj.split('.')[0], obj.split('.')[1])
                                    # elif "<class '" in str(eval(str(obj.split('.')[1].split('.')[0]))):
                                    #     tmp_obj = HOOKING.cls_blt(obj.split('.')[1])
                                    exec(f"__import__('{obj.split('.')[0]}').{obj.split('.')[1]} = tmp_obj", {'tmp_obj': tmp_obj})
                                    del tmp_obj
                            print(f"[+] [HOOK: <{obj}() -> HOOKING>]")
                            print('-'*42)
                        except KeyboardInterrupt:
                            print(f"[!] [ERROR: CANNOT HOOK <{obj}()>]")
                            __import__('builtins').globals = None
                            break
                del i
                if __import__('builtins').globals == None:break
                __cached__ = None
                __name__ = '__main__'
                __doc__ = None
                __package__ = None
                __spec__ = None
                __builtins__ = __import__('builtins')
                __annotations__ = {}
                __loader__ = __import__('builtins').__loader__
                obj = ['__warningregistry__', '__compiled__']
                for i in obj:
                    try:del globals()[i]
                    except:pass
                obj = ['__nuitka_loader_type', '__nuitka_binary_exe', '__nuitka_binary_dir', '_']
                for i in obj:
                    try:del __import__('builtins').__dict__[i]
                    except:pass
                try:del obj, i
                except:pass
                print(cmd)
                try:exec(__import__('builtins').compile(__PyType__, 'HOOKING', 'exec'), globals())
                except ValueError as e:
                    if "bad marshal data (unknown type code)" in str(e):print("""
        >> PYTHON FILE VERSION <<
>> IS DIFFERENT FROM CURRENT VERSION <<
            CAN'T HANDLE!!
""")
                except Exception as e:
                    print('[!] [ERROR:THERE WAS AN ERROR IN THE HOOKING PROCESS]')
                    try:compile(str(e), '<HOOKING-ERROR>', 'exec')
                    except SyntaxError as se:
                        __import__('logging').error('SyntaxError: %s', str(se))
                        error_text = str(se)
                    except Exception as comp_exception:
                        __import__('logging').error('Error: %s', str(comp_exception))
                        error_text = str(comp_exception)
                    if error_text:
                        __import__('logging').error('ChildProcessError: %s', error_text)
                        raise ChildProcessError(error_text)
                    tb = __import__('traceback').format_exc().splitlines()
                    custom_tb = tb[:1] + tb[3:3] + tb[-1:]
                    print("\n".join(custom_tb))
                print(cmd)
                break
            else:del is_ok
        elif chon == "2":
            clear_()
            print(' '*9+"--> [Start hook (Shell)] <--")
            print(cmd)
            if __import__('os').name == 'nt':
                __import__('os').system('title HookLibrary - python >NUL 2>&1')
            __import__('time').sleep(0.4)
            if __import__('os').name == 'nt':print("Python {0} (tags/v{0}) [HookLibrary {1} bit ({2})] on win32".format(__import__('sys').version.split(" ")[0], ("64" if __import__('sys').maxsize > 2**32 else "32"), ("AMD64" if __import__('sys').maxsize > 2**32 else "Intel")))
            else:print("Python {0} (main) [HookLibrary] on linux".format(__import__('sys').version.split(" ")[0]))
            print('Type "help", "copyright", "credits" or "license" for more information.')
            __import__('sys').stdout.write('\033[?25h')
            print('>>> ', end = '')
            __import__('sys').stdout.flush()
            __import__('time').sleep(0.2)
            print('hook.load(os={0},shell=True);del hook'.format(str(str(__import__('os').name).encode('utf8'))[1:]))
            __import__('time').sleep(0.6)
            if 1:
                i = 0
                for obj in MODULE['config']:
                    if MODULE['config'][obj]:
                        try:
                            if obj.split('.')[1] == 'exec' or obj.split('.')[1] == 'eval':
                                if not i:
                                    try:
                                        MinhNguyen2412 = __import__('types').ModuleType('MinhNguyen2412')
                                        for attr in dir(__import__('builtins')):
                                            setattr(MinhNguyen2412, attr, getattr(__import__('builtins'), attr))
                                        __import__('builtins')
                                        MinhNguyen2412.__name__ = __import__('builtins').__name__
                                        MinhNguyen2412.__doc__ = __import__('builtins').__doc__
                                        MinhNguyen2412.__spec__ = __import__('builtins').__spec__
                                        try:
                                            for attr in ['__cached__', '__file__', '__builtins__']:
                                                try:delattr(MinhNguyen2412, attr)
                                                except AttributeError:pass
                                        except:pass
                                        __import__('sys').modules['builtins'] = MinhNguyen2412
                                        __builtins__ = __import__('builtins')
                                        i = 1
                                    except:
                                        raise NameError()
                                if obj.split('.')[1] == 'exec':
                                    tmp_obj = HOOKING.builtinsㅤexec()
                                elif obj.split('.')[1] == 'eval':
                                    tmp_obj = HOOKING.builtinsㅤeval()
                                else:
                                    raise NameError()
                                try:
                                    exec(
                                        "__import__('{0}').{1} = tmp_obj".format(obj.split('.')[0], obj.split('.')[1]), 
                                        {'tmp_obj': tmp_obj}
                                    )
                                except AttributeError:
                                    del tmp_obj
                                    raise NameError()
                                del tmp_obj
                            else:
                                lib = str(obj.split('.')[0]) 
                                try:
                                    exec(f"""__import__('{obj.split('.')[0]}').{obj.split('.')[1]} = HOOKING.{obj.replace(".", "ㅤ")}()""", globals())
                                except AttributeError:
                                    try:
                                        if "<built-in function " in str(eval(str(obj.split('.')[1].split('.')[0]))):
                                            tmp_obj = HOOKING.builtins(obj.split('.')[1])
                                    except NameError:
                                        if 'marshal' not in lib or 'zlib' not in lib or 'binascii' not in lib or 'hashlib' not in lib or 'builtins' not in lib:
                                            tmp_obj = HOOKING.LIBRALY(obj.split('.')[0], obj.split('.')[1])
                                    # elif "<class '" in str(eval(str(obj.split('.')[1].split('.')[0]))):
                                    #     tmp_obj = HOOKING.cls_blt(obj.split('.')[1])
                                    exec(f"__import__('{obj.split('.')[0]}').{obj.split('.')[1]} = tmp_obj", {'tmp_obj': tmp_obj})
                                    del tmp_obj
                            print(f"[+] [HOOK: <{obj}() -> HOOKING>]")
                            print('-'*42)
                        except KeyboardInterrupt:
                            print(f"[!] [ERROR: CANNOT HOOK <{obj}()>]")
                            __import__('builtins').globals = None
                            break
                del i
            if __import__('builtins').globals == None:break
            obj = ['__warningregistry__', '__file__', '__cached__', '__compiled__']
            for i in obj:
                try:del globals()[i]
                except:pass
            obj = ['__nuitka_loader_type', '__nuitka_binary_exe', '__nuitka_binary_dir', '_']
            for i in obj:
                try:del __import__('builtins').__dict__[i]
                except:pass
            try:del obj, i
            except:pass
            __import__('sys').argv = ['']
            __loader__ = __import__('builtins').__loader__
            __builtins__ = __import__('builtins')
            __spec__ = None
            __package__ = None
            __annotations__ = {}
            __name__ = '__main__'
            __doc__ = None
            print('[USE: EXIT() TO EXIT HOOKLIBRARY]')
            print(cmd)
            while 1:
                try:
                    __import__('builtins').inp = input(">>> ")
                    try:__import__('builtins').__dict__
                    except:break
                    if str(__import__('builtins').inp) == "/quit":break
                    _inp_ = __import__('builtins').inp
                    while _inp_.endswith(':') or _inp_.endswith(': ') or _inp_.startswith(' '):
                        _inp_ = input('... ')
                        __import__('builtins').inp += '\n' + _inp_
                    if not __import__('builtins').inp.strip(): continue
                    try:del _inp_
                    except:pass
                    try:__import__('builtins').inp = __import__('builtins').compile.inp[0](__import__('builtins').inp, '<stdin>', 'single')
                    except:
                        try:__import__('builtins').inp = __import__('builtins').compile(__import__('builtins').inp, '<stdin>', 'single')
                        except:pass
                    exec(__import__('builtins').inp)
                except KeyboardInterrupt:print("\nKeyboardInterrupt")
                except Exception:
                    def ERROR():
                        try:
                            traceback = str(__import__('traceback').format_exc()).split("\n")
                            new_traceback = traceback[0] + "\n"
                            for trace in range(2, len(traceback), 1):
                                if "  File " in traceback[trace]:
                                    traceback = new_traceback + "\n".join(traceback[trace:])[:-1]
                                    break
                            traceback = traceback.split("\n")
                            new_traceback = ""
                            is_detect = 0
                            for trace in range(0, len(traceback), 1):
                                if '  File "C:\\MinhNguyen2412.py", line ' in traceback[trace]:is_detect = 1
                                else:
                                    if is_detect:
                                        if traceback[trace][:2] == "  ":
                                            if "  File " == traceback[trace][:7]:
                                                is_detect = 0
                                                continue
                                            else:continue
                                    new_traceback = new_traceback + traceback[trace] + "\n"
                            print(new_traceback[:-1])
                            del traceback, trace, new_traceback, is_detect
                        except KeyboardInterrupt:return None
                    ERROR()
                    try:del ERROR
                    except:pass
        elif chon == "3":
            clear_()
            while 1:
                print(' '*9+f"--> SETTINGS HOOK <--\n{cmd}")
                count = 1
                for opt in MODULE['config']:
                    if 'builtins.type' in f"{opt:20}":method = "BYPASS.ANTI.HOOK"
                    elif 'bypass.layer' in f"{opt:20}":method = "BYPASS.ANTI.LAYER"
                    elif 'marshal.loads' in f"{opt:20}":method = "marshal.loads(3:dis)"
                    elif 'builtins.exec' in f"{opt:20}":method = "builtins.exec(8:view)"
                    else:method = opt
                    print(f" {list(MODULE['config']).index(opt)+1}. [{method:20}] [{MODULE['enabled'] if MODULE['config'][opt] == 1 else MODULE['disabled']}]")
                if count > -1 and count < 10:count = 1
                elif count > 9:count = 2
                elif count > 99:count = 3
                else:count = 0
                print(" 0. [ADD CUSTOM FUNCTION FROM 'builtins']")
                print("     \\________[K]:[BACK]________/")
                print(cmd)
                inp = input("[+] [CHOOSE]: ")
                clear_()
                if inp.lower() == "k":break
                elif inp == "0":
                    clear_()
                    while 1:
                        print("--> [LIST FUNCTION FROM 'builtins'] <--")
                        print(cmd)
                        ds_blt = []
                        list_library = []
                        builtins_dict = __import__('builtins').__dict__
                        cls = ['bool', 'memoryview', 'bytearray', 
                                'bytes', 'classmethod', 'complex',
                                'dict', 'enumerate', 'filter', 'float',
                                'frozenset', 'property', 'int', 'list',
                                'map', 'object', 'range', 'reversed',
                                'set', 'slice', 'staticmethod', 'str',
                                'super', 'tuple', 'type', 'zip'
                                ]
                        for obj in MODULE['config']:
                            if 'bypass' not in str(obj.split('.')[0]):
                                if "<module '" in str(eval(f"__import__('{obj.split('.')[0]}')")) and 'builtins' not in str(obj.split('.')[0]):
                                    list_library.append(f"{obj.split('.')[0]}.{obj.split('.')[1]}")
                        count = 0
                        color = ""
                        for item in builtins_dict:
                            if "<built-in function " in str(builtins_dict[item]):
                                if item not in ["__import__", "__build_class__"]:
                                    ds_blt.append(item)
                        # for item in range(len(cls)):
                        #     ds_blt.append(cls[item])
                        for item in range(len(ds_blt)):
                            if f"builtins.{ds_blt[item]}" in MODULE['config']:
                                color = __import__('colorama').Fore.RED
                            else:
                                color = __import__('colorama').Fore.GREEN
                            if count == 4:
                                print("")
                                count = 0
                            print("{0} [{1}{2}{0}]{3}".format(__import__('colorama').Fore.CYAN, color, str(ds_blt[item]), __import__('colorama').Style.RESET_ALL),end='')
                            count += 1
                        print()
                        print('-'*42)
                        print("--> [LIST FUNCTION FROM 'library'] <--")
                        print(cmd)
                        count = 0
                        color = ""
                        for item in range(len(list_library)):
                            if f"{list_library[item].split('.')[0]}.{list_library[item].split('.')[1]}" in MODULE['config']:
                                color = __import__('colorama').Fore.RED
                            else:
                                color = __import__('colorama').Fore.GREEN
                            if count == 2:
                                print("")
                                count = 0
                            print("{0} [{1}{2}{0}]{3}".format(__import__('colorama').Fore.CYAN, color, str(list_library[item]), __import__('colorama').Style.RESET_ALL),end='')
                            count += 1
                        print()
                        print("==> [ex:] (base64.b64decode)")
                        print('-'*42)
                        print("     \\________[K]:[BACK]________/")
                        print(cmd)
                        inp = input("[+] [BUILT-LIBRR IN FUNCTION NAME]: ")
                        if inp.upper() == 'K':
                            clear_()
                            break
                        try:
                            try:
                                if "<built-in function " in str(__import__('builtins').__dict__[inp]): # or inp in cls:
                                    if f"builtins.{inp}" in MODULE['config']:
                                        input(f"[!] [ERROR: ({inp}) ALREADY ADDED]")
                                        clear_()
                                    elif inp == "__import__" or inp == "__build_class__":
                                        input(f"[!] [ERROR: ({inp}) UNSUPPORTED FOR HOOK]")
                                        clear_()
                                    else:
                                        MODULE['config'][f"builtins.{inp}"] = 0
                                        clear_()
                                        print(f"[+] [FUNC ({inp}) HAVE BEEN ADDED]")
                                else:
                                    input(f"[!] [ERROR: ({inp}) IS NOT A BUILT-IN FUNCTION]")
                                    clear_()
                            except (KeyError, ValueError):
                                try:
                                    __import__(inp.split('.')[0])
                                except ModuleNotFoundError:
                                    input("[!] [ERROR: LIBRARY IS NOT INSTALLED]")
                                    clear_()
                                    continue
                                try:
                                    exec(f"__import__('{inp.split('.')[0]}').{inp.split('.')[1]}")
                                except AttributeError:
                                    input("[!] [ERROR: LIBRARY FUNCTION IS NOT CORRECT FORMAT]")
                                    clear_()
                                    continue
                                if inp in MODULE['config']:
                                    input(f"[!] [ERROR: ({inp}) ALREADY ADDED]")
                                    clear_()
                                    continue
                                MODULE['config'][inp] = 0
                                clear_()
                                print(f"[+] [LIBRR ({inp}) HAVE BEEN ADDED]")
                        except (KeyError, IndexError, ValueError, ModuleNotFoundError, SyntaxError):
                            input("[!] [ERROR: UNKNOWN]")
                            clear_()
                else:
                    try:
                        if str(inp) == '3:dis':
                            dk_dis.append(inp.split(':')[1])
                            inp = inp.split(':')[0]
                            MODULE['config'][list(MODULE['config'])[int(inp) - 1]] = not MODULE['config'][list(MODULE['config'])[int(inp) - 1]]
                        elif str(inp) == '8:view':
                            dk_view.append(inp.split(':')[1])
                            inp = inp.split(':')[0]
                            MODULE['config'][list(MODULE['config'])[int(inp) - 1]] = not MODULE['config'][list(MODULE['config'])[int(inp) - 1]]
                        else:
                            MODULE['config'][list(MODULE['config'])[int(inp) - 1]] = not MODULE['config'][list(MODULE['config'])[int(inp) - 1]]
                    except (IndexError, ValueError):pass
        elif chon.lower() == "k":
            chon = None
            __import__('sys').exit(0)
        else:clear_()
except SystemExit:pass
except KeyboardInterrupt:
    print("\n\nKeyboardInterrupt")
    pass
except Exception as e:
    try:
        try:
            MODULE['config']
            print("ERROR: {0}".format(str(__import__('traceback').format_exc())))
        except:
            def ERROR():
                try:
                    traceback = str(__import__('traceback').format_exc()).split("\n")
                    new_traceback = traceback[0] + "\n"
                    for trace in range(2, len(traceback)):
                        if "File " in traceback[trace]:
                            new_traceback = new_traceback + "\n".join(traceback[trace:])
                            break
                    print(new_traceback[:-1])
                    del traceback, trace
                except:return None
            ERROR()
            del ERROR
    except:pass
try:__import__("shutil").rmtree(f'{__pypath__}/__pycache__')
except:pass
try:
    __import__('sys').stdout.write("\n>> Pause terminal! Press any key to continue\n")
    __import__('sys').stdout.flush()
    __import__('msvcrt').getch()
except:pass
__import__('sys').exit()
