name = "usd_core"

version = "19.07"

authors = [
    "Pixar"
]

description = \
    """
    USD core libraries and binaries from Pixar's repository.
    """

requires = [
    "alembic-1.7+",
    "boost-1.61+",
    "cmake-3+",
    "gcc-6+",
    "glew-2+",
    "ilmbase-2.2+<2.4",
    "jinja2-2+",
    "ocio-1.0.9+",
    "openexr-2.2+<2.4",
    "oiio-1.7.14+",
    "opensubdiv-3.3+",
    "ptex-2.1+",
    "pyopengl-3+",
    "pyside2-5.12",
    "python-2.7+<3",
    "tbb-2017.U6+",
]

variants = [
    ["platform-linux"]
]

tools = [
    "sdfdump",
    "sdffilter",
    "usdcat",
    "usdchecker",
    "usddiff",
    "usddumpcrate",
    "usdedit",
    "usdGenSchema",
    "usdrecord",
    "usdresolve",
    "usdstitch",
    "usdstitchclips",
    "usdtree",
    "usdzip"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "usd_core-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python")
    env.CMAKE_MODULE_PATH.prepend("{root}")

    # Helper environment variables.
    env.USD_BINARY_PATH.set("{root}/bin")
    env.USD_INCLUDE_PATH.set("{root}/include")
    env.USD_LIBRARY_PATH.set("{root}/lib")
