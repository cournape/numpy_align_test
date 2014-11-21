from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration


def configuration(parent_package='', top_path=None):
    config = Configuration('dummy', parent_package, top_path)

    config.add_library('dummy', sources=["dummy.f"])

    config.add_extension('_dummy',
                         sources='dummy.pyf',
                         libraries=['dummy'])
    return config


if __name__ == '__main__':
    setup(**configuration(top_path='').todict())
