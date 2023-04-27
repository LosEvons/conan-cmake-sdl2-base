import subprocess

def RunConan(build_type):
    subprocess.run((
        'conan', 'install', '.',
        '--build', 'missing',
        '--output-folder=./conan',
    	f'--settings=build_type={build_type}',
		'-c', 'tools.system.package_manager:mode=install',
		'-c', 'tools.system.package_manager:sudo=true'
    ))

def RunCmake():
    subprocess.run((
		'cmake',
		'-S', '.',
		'-B', './build'
	))

if __name__ == "__main__":
    RunConan("Debug")
    RunConan("Release")
    RunCmake()