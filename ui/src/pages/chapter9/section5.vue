<template>
  <v-card>
    <v-tabs
      v-model="tab"
      bg-color="primary"
    >
      <v-tab value="keqian">
        课前
      </v-tab>
      <v-tab value="kehou">
        课后
      </v-tab>
    </v-tabs>

    <v-card-text>
      <v-tabs-window v-model="tab">
        <v-tabs-window-item value="keqian">
          <Keqian />
        </v-tabs-window-item>

        <v-tabs-window-item value="kehou">
          <Kehou />
        </v-tabs-window-item>
      </v-tabs-window>
    </v-card-text>
  </v-card>
</template>
<script setup>
import { ref } from 'vue';
import Keqian from '@/components/Keqian.vue';
import Kehou from '@/components/kehou.vue';
const tab = ref(null);

</script>