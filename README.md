# competitive-programming
Data structures and algorithms practise
sorting the sentence


# How to rewrite git commits to another email (from work to personal)

## Rewrite past commits to replace it with your personal one.

git filter-branch --env-filter '
if [ "$GIT_COMMITTER_EMAIL" = "work@example.com" ]
then
    GIT_COMMITTER_EMAIL="personal@example.com"
    GIT_AUTHOR_EMAIL="personal@example.com"
fi
' -- --all

## force push

git push origin --force --all
git push origin --force --tags

