# sql-rewrite
A python script to rewrite sql statements

# usage
icheko/sql-rewrite:1.0 [source file] [destination file] [table name] [value to replace : index] [new value]

For example, this will replace all insert statements for the "public.employers" table.
```
docker run \
    -it \
    --rm \
    -v `pwd`:/usr/src/app/files \
    icheko/sql-rewrite:1.0 "files/seed-data.sql" "files/seed-data-new.sql" "public.employers" 0 'WOOT'
```

From:
```
INSERT INTO public.employers VALUES ('9cdbcb06-b09f-4ed0-b4be-ee42a35a1308', 'test', NULL, NULL, ... );
```
Into:

```
INSERT INTO public.employers VALUES ( WOOT, 'test', NULL, NULL, ... );
```
