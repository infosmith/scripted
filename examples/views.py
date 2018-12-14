"""Github automation."""
import scripted

from .helpers import GithubPublicAPI


script = scripted.Script()


class TerminalView(script.View):

    def options(self, resources):
        """Print repository releases to stdout."""
        for index, resource in enumerate(resources):
            option = " {}".format(str(index + 1).ljust(2))
            self.fn.print(option, resource['name'])


@script.add_controller
class Github(script.Controller):
    """Github convenience."""

    git = GithubPublicAPI()
    view = TerminalView()

    @script.argument('-r', '--release', help='release to be download')
    @script.argument('repo', dest='repo', help='user/repo formatted repository')
    def releases(self):
        """Releases of provided repository."""

        if self.args.release:
            release = self.args.release

        else:
            latest_releases = self.git.releases(self.args.repo)
            self.view.options(latest_releases)
            release = self.view.fn.prompt(' Select release > ')

        self.git.download(self.args.repo, release)


if __name__ == '__main__':
    script.execute()
