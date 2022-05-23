from datetime import datetime
import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
import pathlib
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

relevant_file_types = ['.md']


def git_log_history_command():
    return ['git', 'log', '--numstat',
            '--pretty=format:"%x09%x09%x09%h%x09%at%x09%aN"']


def git_log_projectName_command():
    return ['git', 'remote', '-v']


def run_git_command(command):
    return subprocess.run(command, check=True,
                          stdout=subprocess.PIPE,
                          universal_newlines=True).stdout


def get_project_name():
    project_info = run_git_command(git_log_projectName_command())
    return project_info.replace('\t', ' ').split(' ')[1]


def get_history_data(filename='git.log'):
    git_hist = run_git_command(git_log_history_command())
    git_hist = git_hist.replace('"', ' ')
    with open(filename, 'w') as fp:
        fp.write(git_hist)
    names = ['additions', 'deletions', 'filename', 'sha', 'timestamp', 'author']
    git_log = pd.read_csv(filename, sep="\t", header=None, names=names)
    git_log = git_log[['additions', 'deletions', 'filename']]\
            .join(git_log[['sha', 'timestamp', 'author']]\
            .fillna(method='ffill'))\
            .dropna()
    git_log['timestamp'] = pd.to_datetime(git_log.timestamp, unit='s')
    git_log.set_index('timestamp', inplace=True)
    git_log['extention'] = git_log.filename.apply(lambda path: pathlib.PurePosixPath(path).suffix)
    git_log.loc[git_log['additions'] == '-', 'additions'] = np.nan
    git_log.loc[git_log['deletions'] == '-', 'deletions'] = np.nan
    git_log['line_count'] = git_log.additions.astype(float) -\
                            git_log.deletions.astype(float)
    git_log.loc[:, 'commit_count'] = 1
    print("Found {0} commits in project's history".format(git_log.sha.unique().shape[0]))
    return git_log


def generate_diagram(project_name, data, interval, filename):
    df = data[["line_count", "commit_count"]].resample(interval)\
          .agg({"line_count": "sum", "commit_count": "sum"})
    df['line_count_cumsum'] = df.line_count.cumsum().astype('int')
    df.drop(["line_count"], axis=1, inplace=True)
    if df.shape[0] > 1:
        fig, ax = plt.subplots(2, 1)
        ax[0].set_title(project_name)
        df.commit_count.plot.bar(label='Commit count', ax=ax[0], grid=True)
        ax[0].grid(True)
        ax[0].set_xticks([])
        ax[0].set_xlabel("")
        ax[0].set_ylabel("Commits")
        df.line_count_cumsum.plot(drawstyle="steps-mid", ax=ax[1], grid=True)
        ax[1].set_ylabel("Lines of code")
        plt.tight_layout()
        # plt.show()
        fig.savefig(filename+".png")
        print("File saved to " + filename + ".png")
    else:
        print("Not enought data for printing `" + interval + "` diagram")


if __name__ == "__main__":
    project_name = get_project_name()
    print("Evaluating project " + project_name)
    data = get_history_data()
    filtered = data[data.extention.isin(relevant_file_types)]
    intervals = {
        "Day": 'D',
        "Week": "W",
        "Month": 'M',
        "Year": 'Y'}
    for name, abbrevation in intervals.items():
        generate_diagram(project_name, filtered, abbrevation, name)
    print("Aus die Maus!")