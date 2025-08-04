import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://your-bucket/healthcare/raw/"], "recurse": True},
    format_options={"withHeader": True}
)

cleaned = df.drop_nulls()

glueContext.write_dynamic_frame.from_options(
    frame=cleaned,
    connection_type="redshift",
    connection_options={
        "url": "jdbc:redshift://your-cluster.amazonaws.com:5439/yourdb",
        "user": "your_user",
        "password": "your_password",
        "dbtable": "public.patient_data",
        "redshiftTmpDir": "s3://your-temp-dir/"
    },
    format="csv"
)

job.commit()
