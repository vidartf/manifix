

"""Create a distutils command wrapper for checking generated files"""


from .check import check_filelist
from .log import init_logging

def manifix_sidst_command(original_command, known_excludes=None, callback=None):
    """Create a manifix setup sdist command

    Parameters
    ----------
    original_command: Command class
        The original command to override.
    known_excludes:

    callback: function, optional
        Override for the callback to call with the generated file list.
    """

    if callback is None:
        callback = check_filelist

    # Ensure logging if not already configured:
    init_logging()

    class ManifixSdistCommand(original_command):
        def make_distribution(self):
            ret = callback(self.filelist, known_excludes=known_excludes)
            if ret:
                raise RuntimeError('Manifix detected some errors, see the error log for details')

    return ManifixSdistCommand
