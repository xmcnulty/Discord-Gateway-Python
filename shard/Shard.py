class Shard:
    def __init__(self, shard_id, num_shards):
        self.shard_id = shard_id
        self.num_shards = num_shards

    # Array of shard_id and num_shards per the Discord Gateway docs
    @property
    def shard_array(self):
        return [self.shard_id, self.num_shards]
