import asyncio
from pathlib import Path

from malloy import Runtime
from malloy.data.bigquery import BigQueryConnection

async def main():
  home_dir = f"{(Path(__file__).parent)}"
  print(home_dir)
#   with Runtime() as malloy_runtime:
#     malloy_runtime.add_connection(BigQueryConnection())

#     malloy_runtime.load_file("hackernews/hackernews.malloy")
#     data = await malloy_runtime.run(query="run: stories->posts_over_time")
#     print(data.to_dataframe())

if __name__ == "__main__":
  asyncio.run(main())
