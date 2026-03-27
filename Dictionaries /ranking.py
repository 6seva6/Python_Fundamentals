existing_contest = {}
while (contest:= input()) != 'end of contests':
    contest = contest.split(':')
    existing_contest [contest[0]] = {'password' : contest[1]}

def is_valid_submission(submission_parts_, existing_contest_, persons_submissions_):
    sub_name, password, person_name, points = submission_parts_
    points = int(points)

    if sub_name in existing_contest_ and password == existing_contest_[sub_name]['password']:
        persons_submissions_.setdefault(person_name, {})

        if sub_name not in persons_submissions_[person_name]:
            persons_submissions_[person_name][sub_name] = points

        elif persons_submissions_[person_name][sub_name] < points:
            persons_submissions_[person_name][sub_name] = points

        return persons_submissions_


persons_submissions = {}
while (submission:= input()) != 'end of submissions':
    submission_parts = submission.split('=>')

    is_valid_submission(submission_parts, existing_contest, persons_submissions)

max_points = 0
person_name = ''

for name, sub_name in persons_submissions.items():
    total = sum(sub_name.values())
    if total > max_points:
        max_points = total
        person_name = name

print(f'Best candidate is {person_name} with total {max_points} points.')
print(f'Ranking:')

for name in sorted(persons_submissions):
    print(f'{name}')
    for contest, points in sorted(persons_submissions[name].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest} -> {points}")
