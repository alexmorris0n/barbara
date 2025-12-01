<template>
  <div class="testy-control">
    <!-- Page Header -->
    <header class="page-header">
      <div class="header-content">
        <div class="title-section">
          <n-icon size="28" color="#8b5cf6"><FlaskOutline /></n-icon>
          <div>
            <h1>Testy McTesterson</h1>
            <p class="subtitle">Test Control Panel</p>
          </div>
        </div>
        <div class="header-actions">
          <button @click="showTestCallModal = true" class="btn-webrtc">
            <n-icon size="18"><HeadsetOutline /></n-icon>
            <span>Browser Call</span>
          </button>
          <button @click="triggerOutboundCall" class="btn-call" :disabled="loading || callingTesty || !state?.lead_id">
            <n-icon size="18"><CallOutline /></n-icon>
            <span v-if="!callingTesty">Call Testy</span>
            <span v-else>Calling...</span>
          </button>
          <button @click="loadState" class="btn-secondary" :disabled="loading">
            <n-icon size="18"><RefreshOutline /></n-icon>
            <span v-if="!loading">Refresh</span>
            <span v-else>Loading...</span>
          </button>
        </div>
      </div>
    </header>

    <!-- Current State Card -->
    <div class="card state-card">
      <div class="card-header">
        <h2><n-icon size="20"><PersonCircleOutline /></n-icon> Current State</h2>
      </div>

      <div v-if="state" class="state-grid">
        <!-- Identity Row -->
        <div class="state-section">
          <div class="state-item">
            <span class="label">Phone</span>
            <span class="value mono">{{ state.phone_number }}</span>
          </div>
          <div class="state-item">
            <span class="label">Lead Name</span>
            <span class="value">{{ state.lead_name || 'N/A' }}</span>
          </div>
          <div class="state-item wide">
            <span class="label">Lead ID</span>
            <span class="value mono small">{{ state.lead_id || 'N/A' }}</span>
          </div>
        </div>

        <!-- Call Status Row -->
        <div class="state-section">
          <div class="state-item">
            <span class="label">Current Node</span>
            <span class="badge" :class="nodeClass">{{ state.current_node || 'NULL' }}</span>
          </div>
          <div class="state-item">
            <span class="label">Call Count</span>
            <span class="value">{{ state.call_count ?? 0 }}</span>
          </div>
          <div class="state-item">
            <span class="label">Call Status</span>
            <span class="badge" :class="callStatusClass">{{ state.call_status || 'N/A' }}</span>
          </div>
          <div class="state-item">
            <span class="label">Exit Reason</span>
            <span class="value">{{ state.exit_reason || 'N/A' }}</span>
          </div>
        </div>

        <!-- Timestamps Row -->
        <div class="state-section">
          <div class="state-item">
            <span class="label">Last Call</span>
            <span class="value">{{ formatDate(state.last_call_at) }}</span>
          </div>
          <div class="state-item">
            <span class="label">Last Updated</span>
            <span class="value">{{ formatDate(state.updated_at) }}</span>
          </div>
        </div>

        <!-- Core Flags -->
        <div class="flags-section">
          <div class="flag-chip" :class="state.qualified ? 'flag-success' : 'flag-error'">
            <n-icon size="14">
              <CheckmarkCircle v-if="state.qualified" />
              <CloseCircle v-else />
            </n-icon>
            <span>Qualified</span>
          </div>
          <div class="flag-chip" :class="state.verified ? 'flag-success' : 'flag-error'">
            <n-icon size="14">
              <CheckmarkCircle v-if="state.verified" />
              <CloseCircle v-else />
            </n-icon>
            <span>Verified</span>
          </div>
          <div class="flag-chip" :class="state.quote_presented ? 'flag-success' : 'flag-error'">
            <n-icon size="14">
              <CheckmarkCircle v-if="state.quote_presented" />
              <CloseCircle v-else />
            </n-icon>
            <span>Quote Presented</span>
          </div>
          <div class="flag-chip" :class="state.ready_to_book ? 'flag-success' : 'flag-error'">
            <n-icon size="14">
              <CheckmarkCircle v-if="state.ready_to_book" />
              <CloseCircle v-else />
            </n-icon>
            <span>Ready to Book</span>
          </div>
          <div class="flag-chip" :class="state.wrong_person ? 'flag-warning' : 'flag-neutral'">
            <n-icon size="14">
              <AlertCircle v-if="state.wrong_person" />
              <CheckmarkCircle v-else />
            </n-icon>
            <span>Wrong Person</span>
          </div>
        </div>

        <!-- Quote Details -->
        <div v-if="state.quote_lump_sum || state.quote_monthly" class="quote-card">
          <n-icon size="20" color="#10b981"><CashOutline /></n-icon>
          <span class="quote-value">
            {{ state.quote_lump_sum ? `$${Number(state.quote_lump_sum).toLocaleString()} lump sum` : '' }}
            {{ state.quote_lump_sum && state.quote_monthly ? ' / ' : '' }}
            {{ state.quote_monthly ? `$${Number(state.quote_monthly).toLocaleString()}/mo` : '' }}
          </span>
        </div>

        <!-- Verification Badges -->
        <div class="verification-row">
          <span class="label">Verification:</span>
          <div class="verification-badges">
            <span class="mini-badge" :class="state.phone_verified ? 'mini-success' : 'mini-inactive'">
              <n-icon size="12"><PhonePortraitOutline /></n-icon> Phone
            </span>
            <span class="mini-badge" :class="state.email_verified ? 'mini-success' : 'mini-inactive'">
              <n-icon size="12"><MailOutline /></n-icon> Email
            </span>
            <span class="mini-badge" :class="state.address_verified ? 'mini-success' : 'mini-inactive'">
              <n-icon size="12"><HomeOutline /></n-icon> Address
            </span>
          </div>
        </div>
      </div>

      <!-- Conversation Data (Normalized) -->
      <div v-if="normalizedConversationData.length > 0" class="json-section">
        <h3><n-icon size="16"><CodeSlashOutline /></n-icon> Conversation Context</h3>
        <div class="context-groups">
          <!-- Flow State -->
          <div v-if="contextGroups.flow.length" class="context-group">
            <div class="context-group-label">Flow</div>
            <div class="context-chips">
              <span v-for="item in contextGroups.flow" :key="item.key" 
                    class="context-chip" :class="getChipClass(item.value)">
                {{ item.label }}
              </span>
            </div>
          </div>
          
          <!-- Quote Info -->
          <div v-if="contextGroups.quote.length" class="context-group">
            <div class="context-group-label">Quote</div>
            <div class="context-items">
              <div v-for="item in contextGroups.quote" :key="item.key" class="context-item">
                <span class="context-key">{{ item.label }}</span>
                <span class="context-value">{{ item.displayValue }}</span>
              </div>
            </div>
          </div>
          
          <!-- Wrong Person -->
          <div v-if="contextGroups.wrongPerson.length" class="context-group">
            <div class="context-group-label">Wrong Person</div>
            <div class="context-items">
              <div v-for="item in contextGroups.wrongPerson" :key="item.key" class="context-item">
                <span class="context-key">{{ item.label }}</span>
                <span class="context-value">{{ item.displayValue }}</span>
              </div>
            </div>
          </div>
          
          <!-- Call Info -->
          <div v-if="contextGroups.call.length" class="context-group">
            <div class="context-group-label">Call Info</div>
            <div class="context-items">
              <div v-for="item in contextGroups.call" :key="item.key" class="context-item">
                <span class="context-key">{{ item.label }}</span>
                <span class="context-value">{{ item.displayValue }}</span>
              </div>
            </div>
          </div>
          
          <!-- Other -->
          <div v-if="contextGroups.other.length" class="context-group">
            <div class="context-group-label">Other</div>
            <div class="context-items">
              <div v-for="item in contextGroups.other" :key="item.key" class="context-item">
                <span class="context-key">{{ item.label }}</span>
                <span class="context-value" :class="getValueClass(item.value)">{{ item.displayValue }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-if="!state && !loading" class="empty-state">
        <n-icon size="48" color="rgba(255,255,255,0.3)"><AlertCircleOutline /></n-icon>
        <p>No state found. Click "Reset to Fresh" to initialize.</p>
      </div>
    </div>

    <!-- Quick Actions -->
    <div class="card">
      <div class="card-header">
        <h2><n-icon size="20"><FlashOutline /></n-icon> Quick Actions</h2>
      </div>
      <div class="actions-grid">
        <button @click="resetFresh" class="action-btn action-primary" :disabled="loading">
          <n-icon size="20"><RefreshCircleOutline /></n-icon>
          <span>Reset to Fresh</span>
          <small>Empty State</small>
        </button>
        
        <button @click="setQualified" class="action-btn action-success" :disabled="loading">
          <n-icon size="20"><CheckmarkCircleOutline /></n-icon>
          <span>Set Qualified</span>
          <small>Skip to ANSWER</small>
        </button>
        
        <button @click="setReadyToBook" class="action-btn action-info" :disabled="loading">
          <n-icon size="20"><CalendarOutline /></n-icon>
          <span>Ready to Book</span>
          <small>Skip to BOOK</small>
        </button>
        
        <button @click="clearAppointment" class="action-btn action-warning" :disabled="loading">
          <n-icon size="20"><TrashOutline /></n-icon>
          <span>Clear Appointment</span>
          <small>Remove booking</small>
        </button>
        
        <button @click="deleteState" class="action-btn action-danger" :disabled="loading">
          <n-icon size="20"><CloseCircleOutline /></n-icon>
          <span>Delete All State</span>
          <small>Full reset</small>
        </button>
      </div>
    </div>

    <!-- Test Scenarios -->
    <div class="card">
      <div class="card-header">
        <h2><n-icon size="20"><GitBranchOutline /></n-icon> Test Scenarios</h2>
      </div>
      <div class="scenarios-grid">
        <div class="scenario-card" @click="applyPreset('new_caller')" :class="{ disabled: loading }">
          <div class="scenario-icon"><n-icon size="28"><AddCircleOutline /></n-icon></div>
          <div class="scenario-title">New Caller</div>
          <div class="scenario-desc">No history, start from GREET</div>
        </div>

        <div class="scenario-card" @click="applyPreset('has_questions')" :class="{ disabled: loading }">
          <div class="scenario-icon"><n-icon size="28"><HelpCircleOutline /></n-icon></div>
          <div class="scenario-title">Has Questions</div>
          <div class="scenario-desc">Start from ANSWER context</div>
        </div>

        <div class="scenario-card" @click="applyPreset('ready_to_book')" :class="{ disabled: loading }">
          <div class="scenario-icon"><n-icon size="28"><CalendarOutline /></n-icon></div>
          <div class="scenario-title">Ready to Book</div>
          <div class="scenario-desc">Start from BOOK context</div>
        </div>

        <div class="scenario-card" @click="applyPreset('returning_caller')" :class="{ disabled: loading }">
          <div class="scenario-icon"><n-icon size="28"><ArrowBackCircleOutline /></n-icon></div>
          <div class="scenario-title">Returning Caller</div>
          <div class="scenario-desc">Already qualified, skip to ANSWER</div>
        </div>

        <div class="scenario-card" @click="applyPreset('wrong_person')" :class="{ disabled: loading }">
          <div class="scenario-icon"><n-icon size="28"><PersonRemoveOutline /></n-icon></div>
          <div class="scenario-title">Wrong Person</div>
          <div class="scenario-desc">Test wrong person flow</div>
        </div>

        <div class="scenario-card" @click="applyPreset('quote_presented')" :class="{ disabled: loading }">
          <div class="scenario-icon"><n-icon size="28"><CashOutline /></n-icon></div>
          <div class="scenario-title">Quote Presented</div>
          <div class="scenario-desc">Has seen quote, not yet booked</div>
        </div>
      </div>
    </div>

    <!-- Success/Error Toast -->
    <transition name="toast">
      <div v-if="message" class="toast" :class="messageType">
        <n-icon size="18"><component :is="messageType === 'success' ? CheckmarkCircle : AlertCircle" /></n-icon>
        {{ message }}
      </div>
    </transition>

    <!-- WebRTC Test Call Modal -->
    <TestCallModal
      :show="showTestCallModal"
      mode="full"
      start-node="greet"
      vertical="reverse_mortgage"
      @close="showTestCallModal = false"
    />
  </div>
</template>

<script>
import { supabase } from '@/lib/supabase'
import { NIcon } from 'naive-ui'
import TestCallModal from '@/components/TestCallModal.vue'
import {
  FlaskOutline,
  CallOutline,
  RefreshOutline,
  PersonCircleOutline,
  CheckmarkCircle,
  CloseCircle,
  AlertCircle,
  AlertCircleOutline,
  CashOutline,
  PhonePortraitOutline,
  MailOutline,
  HomeOutline,
  CodeSlashOutline,
  FlashOutline,
  RefreshCircleOutline,
  CheckmarkCircleOutline,
  CalendarOutline,
  TrashOutline,
  CloseCircleOutline,
  GitBranchOutline,
  AddCircleOutline,
  HelpCircleOutline,
  ArrowBackCircleOutline,
  PersonRemoveOutline,
  HeadsetOutline
} from '@vicons/ionicons5'

// Testy phone numbers - E.164 for leads table, 10-digit for conversation_state
const TESTY_PHONE_E164 = '+16505300051'
const TESTY_PHONE_10DIGIT = '6505300051'

export default {
  name: 'TestyControl',
  components: {
    NIcon,
    TestCallModal,
    FlaskOutline,
    CallOutline,
    RefreshOutline,
    PersonCircleOutline,
    CheckmarkCircle,
    CloseCircle,
    AlertCircle,
    AlertCircleOutline,
    CashOutline,
    PhonePortraitOutline,
    MailOutline,
    HomeOutline,
    CodeSlashOutline,
    FlashOutline,
    RefreshCircleOutline,
    CheckmarkCircleOutline,
    CalendarOutline,
    TrashOutline,
    CloseCircleOutline,
    GitBranchOutline,
    AddCircleOutline,
    HelpCircleOutline,
    ArrowBackCircleOutline,
    PersonRemoveOutline,
    HeadsetOutline
  },
  data() {
    return {
      state: null,
      loading: false,
      callingTesty: false,
      message: '',
      messageType: 'success',
      supabase,
      showTestCallModal: false
    }
  },
  computed: {
    nodeClass() {
      if (!this.state?.current_node) return 'badge-neutral'
      const node = this.state.current_node.toLowerCase()
      if (node.includes('greet')) return 'badge-info'
      if (node.includes('qualify')) return 'badge-warning'
      if (node.includes('answer')) return 'badge-primary'
      if (node.includes('book')) return 'badge-success'
      if (node.includes('goodbye')) return 'badge-neutral'
      return 'badge-neutral'
    },
    callStatusClass() {
      if (!this.state?.call_status) return 'badge-neutral'
      const status = this.state.call_status.toLowerCase()
      if (status === 'active' || status === 'in_progress') return 'badge-success'
      if (status === 'completed') return 'badge-neutral'
      if (status === 'fresh' || status === 'new') return 'badge-info'
      return 'badge-neutral'
    },
    
    // Normalize conversation_data for display
    normalizedConversationData() {
      if (!this.state?.conversation_data) return []
      
      const data = this.state.conversation_data
      const labelMap = {
        greeted: 'Greeted',
        verified: 'Verified',
        qualified: 'Qualified',
        questions_answered: 'Questions Answered',
        objection_handled: 'Objection Handled',
        quote_presented: 'Quote Shown',
        ready_to_book: 'Ready to Book',
        wrong_person: 'Wrong Person',
        right_person_available: 'Right Person Available',
        wrong_person_relationship: 'Relationship',
        quote_reaction: 'Quote Reaction',
        quote_lump_sum: 'Lump Sum',
        quote_monthly: 'Monthly',
        estimated_lump_sum: 'Est. Lump Sum',
        estimated_monthly: 'Est. Monthly',
        reason_summary: 'Call Reason',
        greeting_reason: 'Greeting Context',
        node_before_objection: 'Node Before Objection',
        answer_turn_count: 'Answer Turns',
        appointment_booked: 'Appointment Booked',
        appointment_id: 'Appointment ID'
      }
      
      // Fields to exclude (already shown in UI)
      const excludeFields = ['quote_lump_sum', 'quote_monthly']
      
      return Object.entries(data)
        .filter(([key]) => !excludeFields.includes(key))
        .map(([key, value]) => ({
          key,
          label: labelMap[key] || this.formatKey(key),
          value,
          displayValue: this.formatDisplayValue(key, value)
        }))
    },
    
    // Group conversation data by category
    contextGroups() {
      const items = this.normalizedConversationData
      
      const flowKeys = ['greeted', 'verified', 'qualified', 'questions_answered', 'objection_handled', 'quote_presented', 'ready_to_book', 'appointment_booked']
      const quoteKeys = ['quote_reaction', 'estimated_lump_sum', 'estimated_monthly']
      const wrongPersonKeys = ['wrong_person', 'right_person_available', 'wrong_person_relationship']
      const callKeys = ['reason_summary', 'greeting_reason', 'answer_turn_count', 'node_before_objection']
      
      return {
        flow: items.filter(i => flowKeys.includes(i.key) && i.value === true),
        quote: items.filter(i => quoteKeys.includes(i.key) && i.value),
        wrongPerson: items.filter(i => wrongPersonKeys.includes(i.key) && i.value),
        call: items.filter(i => callKeys.includes(i.key) && i.value),
        other: items.filter(i => 
          !flowKeys.includes(i.key) && 
          !quoteKeys.includes(i.key) && 
          !wrongPersonKeys.includes(i.key) && 
          !callKeys.includes(i.key) &&
          i.value !== false && i.value !== null && i.value !== undefined
        )
      }
    }
  },
  mounted() {
    this.loadState()
  },
  methods: {
    async loadState() {
      this.loading = true
      try {
        // Get conversation state (uses 10-digit normalized phone)
        const { data: convState, error: convError } = await this.supabase
          .from('conversation_state')
          .select('*')
          .eq('phone_number', TESTY_PHONE_10DIGIT)
          .maybeSingle()

        if (convError) {
          console.error('Conv state error:', convError)
        }

        // Get lead info (uses E.164 format, limit 1 for duplicates)
        const { data: leads, error: leadError } = await this.supabase
          .from('leads')
          .select('id, first_name, last_name, status, verified, phone_verified, email_verified, address_verified')
          .eq('primary_phone_e164', TESTY_PHONE_E164)
          .order('created_at', { ascending: false })
          .limit(1)

        const lead = leads?.[0] || null

        if (leadError) {
          console.error('Lead error:', leadError)
        }

        const convData = convState?.conversation_data || {}

        this.state = {
          phone_number: TESTY_PHONE_E164,
          lead_id: lead?.id || convState?.lead_id,
          lead_name: lead ? `${lead.first_name} ${lead.last_name}` : null,
          current_node: convState?.current_node,
          call_count: convState?.call_count ?? 0,
          call_status: convState?.call_status,
          exit_reason: convState?.exit_reason,
          last_call_at: convState?.last_call_at,
          updated_at: convState?.updated_at,
          qualified: convState?.qualified,
          topics_discussed: convState?.topics_discussed || [],
          conversation_data: convData,
          verified: lead?.verified || convData.verified || false,
          quote_presented: convData.quote_presented || false,
          ready_to_book: convData.ready_to_book || false,
          wrong_person: convData.wrong_person || false,
          quote_lump_sum: convData.quote_lump_sum,
          quote_monthly: convData.quote_monthly,
          phone_verified: lead?.phone_verified || false,
          email_verified: lead?.email_verified || false,
          address_verified: lead?.address_verified || false,
          lead_status: lead?.status
        }
      } catch (error) {
        console.error('Error loading state:', error)
        this.showMessage('Error loading state: ' + error.message, 'error')
      } finally {
        this.loading = false
      }
    },

    async triggerOutboundCall() {
      if (!this.state?.lead_id) {
        this.showMessage('No lead ID found. Reset state first.', 'error')
        return
      }

      if (!confirm('Trigger outbound call to Testy via SignalWire?')) return

      this.callingTesty = true
      try {
        const CLI_TESTING_URL = import.meta.env.VITE_CLI_TESTING_URL || 'https://barbara-cli-testing.fly.dev'
        
        const response = await fetch(`${CLI_TESTING_URL}/trigger-call`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            to_phone: TESTY_PHONE_E164,
            lead_id: this.state.lead_id
          })
        })

        const result = await response.json()
        
        if (result.success || result.call_id) {
          this.showMessage(`Call initiated! SID: ${result.call_id}`, 'success')
        } else {
          throw new Error(result.message || result.error || 'Call failed')
        }
      } catch (error) {
        console.error('Error triggering call:', error)
        this.showMessage('Failed to trigger call: ' + error.message, 'error')
      } finally {
        this.callingTesty = false
      }
    },

    async resetFresh() {
      if (!confirm('Reset Testy to fresh state (no conversation history)?')) return
      
      this.loading = true
      try {
        let leadId = this.state?.lead_id
        
        if (!leadId) {
          const { data: existingLeads } = await this.supabase
            .from('leads')
            .select('id')
            .eq('primary_phone_e164', TESTY_PHONE_E164)
            .order('created_at', { ascending: false })
            .limit(1)
          
          if (existingLeads?.[0]) {
            leadId = existingLeads[0].id
          } else {
            const { data: newLead, error: leadCreateError } = await this.supabase
              .from('leads')
              .insert({
                first_name: 'Testy',
                last_name: 'McTesterson',
                primary_phone: '(650) 530-0051',
                primary_phone_e164: TESTY_PHONE_E164,
                email: 'testy@test.com',
                status: 'new',
                verified: false,
                phone_verified: false,
                email_verified: false,
                address_verified: false,
                source: 'test_panel'
              })
              .select('id')
              .single()
            
            if (leadCreateError) throw leadCreateError
            leadId = newLead.id
          }
        }

        const { data: existing } = await this.supabase
          .from('conversation_state')
          .select('id')
          .eq('phone_number', TESTY_PHONE_10DIGIT)
          .maybeSingle()

        if (existing) {
          const { error: convError } = await this.supabase
            .from('conversation_state')
            .update({
              qualified: null,
              current_node: null,
              conversation_data: {},
              call_count: 0,
              call_status: 'fresh',
              exit_reason: null,
              topics_discussed: [],
              updated_at: new Date().toISOString()
            })
            .eq('phone_number', TESTY_PHONE_10DIGIT)

          if (convError) throw convError
        } else {
          const { error: insertError } = await this.supabase
            .from('conversation_state')
            .insert({
              phone_number: TESTY_PHONE_10DIGIT,
              lead_id: leadId,
              qualified: null,
              current_node: null,
              conversation_data: {},
              call_count: 0,
              call_status: 'fresh',
              exit_reason: null,
              topics_discussed: []
            })
          
          if (insertError) throw insertError
        }

        if (leadId) {
          await this.supabase
            .from('leads')
            .update({
              status: 'new',
              verified: false,
              phone_verified: false,
              email_verified: false,
              address_verified: false,
              updated_at: new Date().toISOString()
            })
            .eq('id', leadId)
        }

        this.showMessage('Reset to fresh state!', 'success')
        await this.loadState()
      } catch (error) {
        console.error('Error resetting:', error)
        this.showMessage('Error: ' + error.message, 'error')
      } finally {
        this.loading = false
      }
    },

    async setQualified() {
      this.loading = true
      try {
        await this.supabase
          .from('conversation_state')
          .update({
            qualified: true,
            current_node: 'answer',
            conversation_data: { greeted: true, verified: true, qualified: true }
          })
          .eq('phone_number', TESTY_PHONE_10DIGIT)

        if (this.state?.lead_id) {
          await this.supabase
            .from('leads')
            .update({ 
              status: 'qualified',
              verified: true,
              phone_verified: true,
              email_verified: true,
              address_verified: true
            })
            .eq('id', this.state.lead_id)
        }

        this.showMessage('Set as qualified!', 'success')
        await this.loadState()
      } catch (error) {
        this.showMessage('Error: ' + error.message, 'error')
      } finally {
        this.loading = false
      }
    },

    async setReadyToBook() {
      this.loading = true
      try {
        await this.supabase
          .from('conversation_state')
          .update({
            qualified: true,
            current_node: 'book',
            conversation_data: {
              greeted: true,
              verified: true,
              qualified: true,
              questions_answered: true,
              ready_to_book: true,
              quote_presented: true,
              quote_lump_sum: 516666,
              quote_monthly: 2152
            }
          })
          .eq('phone_number', TESTY_PHONE_10DIGIT)

        if (this.state?.lead_id) {
          await this.supabase
            .from('leads')
            .update({ 
              status: 'qualified',
              verified: true,
              phone_verified: true,
              email_verified: true,
              address_verified: true
            })
            .eq('id', this.state.lead_id)
        }

        this.showMessage('Set ready to book!', 'success')
        await this.loadState()
      } catch (error) {
        this.showMessage('Error: ' + error.message, 'error')
      } finally {
        this.loading = false
      }
    },

    async clearAppointment() {
      this.loading = true
      try {
        const currentData = { ...this.state.conversation_data }
        delete currentData.appointment_booked
        delete currentData.appointment_id
        delete currentData.ready_to_book

        await this.supabase
          .from('conversation_state')
          .update({ conversation_data: currentData, current_node: 'answer' })
          .eq('phone_number', TESTY_PHONE_10DIGIT)

        if (this.state?.lead_id) {
          await this.supabase
            .from('leads')
            .update({ status: 'qualified' })
            .eq('id', this.state.lead_id)
        }

        this.showMessage('Appointment cleared!', 'success')
        await this.loadState()
      } catch (error) {
        this.showMessage('Error: ' + error.message, 'error')
      } finally {
        this.loading = false
      }
    },

    async deleteState() {
      if (!confirm('Delete ALL state for Testy? This cannot be undone!')) return
      
      this.loading = true
      try {
        await this.supabase
          .from('conversation_state')
          .delete()
          .eq('phone_number', TESTY_PHONE_10DIGIT)

        this.showMessage('State deleted!', 'success')
        this.state = null
      } catch (error) {
        this.showMessage('Error: ' + error.message, 'error')
      } finally {
        this.loading = false
      }
    },

    async applyPreset(preset) {
      if (this.loading) return
      
      const presets = {
        new_caller: {
          qualified: null,
          current_node: null,
          conversation_data: {},
          call_count: 0,
          call_status: 'fresh',
          lead_status: 'new',
          verified: false
        },
        has_questions: {
          qualified: true,
          current_node: 'answer',
          conversation_data: { greeted: true, verified: true, qualified: true },
          lead_status: 'qualified',
          verified: true
        },
        ready_to_book: {
          qualified: true,
          current_node: 'book',
          conversation_data: {
            greeted: true, verified: true, qualified: true,
            questions_answered: true, ready_to_book: true, quote_presented: true,
            quote_lump_sum: 516666, quote_monthly: 2152
          },
          lead_status: 'qualified',
          verified: true
        },
        returning_caller: {
          qualified: true,
          current_node: 'answer',
          conversation_data: {
            greeted: true, verified: true, qualified: true,
            quote_presented: true, quote_reaction: 'positive',
            quote_lump_sum: 516666, quote_monthly: 2152
          },
          lead_status: 'qualified',
          verified: true
        },
        wrong_person: {
          qualified: null,
          current_node: 'greet',
          conversation_data: { wrong_person: true, right_person_available: true },
          lead_status: 'new',
          verified: false
        },
        quote_presented: {
          qualified: true,
          current_node: 'answer',
          conversation_data: {
            greeted: true, verified: true, qualified: true,
            quote_presented: true, quote_lump_sum: 516666, quote_monthly: 2152
          },
          lead_status: 'qualified',
          verified: true
        }
      }

      const config = presets[preset]
      if (!config) return

      this.loading = true
      try {
        await this.supabase
          .from('conversation_state')
          .update({
            qualified: config.qualified,
            current_node: config.current_node,
            conversation_data: config.conversation_data,
            call_count: config.call_count ?? this.state?.call_count ?? 0,
            call_status: config.call_status || 'completed'
          })
          .eq('phone_number', TESTY_PHONE_10DIGIT)

        if (this.state?.lead_id) {
          await this.supabase
            .from('leads')
            .update({ 
              status: config.lead_status,
              verified: config.verified,
              phone_verified: config.verified,
              email_verified: config.verified,
              address_verified: config.verified
            })
            .eq('id', this.state.lead_id)
        }

        this.showMessage(`Applied ${preset.replace(/_/g, ' ')} preset!`, 'success')
        await this.loadState()
      } catch (error) {
        this.showMessage('Error: ' + error.message, 'error')
      } finally {
        this.loading = false
      }
    },

    showMessage(text, type = 'success') {
      this.message = text
      this.messageType = type
      setTimeout(() => { this.message = '' }, 4000)
    },

    formatDate(dateStr) {
      if (!dateStr) return 'N/A'
      return new Date(dateStr).toLocaleString()
    },

    formatValue(value) {
      if (typeof value === 'boolean') return value ? 'Yes' : 'No'
      if (value === null || value === undefined) return 'null'
      if (typeof value === 'object') return JSON.stringify(value)
      return String(value)
    },

    getValueClass(value) {
      if (typeof value === 'boolean') return value ? 'value-true' : 'value-false'
      return ''
    },
    
    formatKey(key) {
      // Convert snake_case to Title Case
      return key
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ')
    },
    
    formatDisplayValue(key, value) {
      if (typeof value === 'boolean') return value ? 'Yes' : 'No'
      if (value === null || value === undefined) return '—'
      
      // Format money values
      if (key.includes('lump_sum') || key.includes('monthly')) {
        const num = Number(value)
        if (!isNaN(num)) return '$' + num.toLocaleString()
      }
      
      // Format counts
      if (key.includes('count')) {
        return String(value)
      }
      
      if (typeof value === 'object') return JSON.stringify(value)
      
      // Convert snake_case string values to Title Case
      const str = String(value)
      if (str.includes('_')) {
        return str.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')
      }
      
      return str
    },
    
    getChipClass(value) {
      if (value === true) return 'chip-success'
      if (value === false) return 'chip-error'
      return 'chip-neutral'
    }
  }
}
</script>

<style scoped>
.testy-control {
  padding: 1.5rem;
  margin: -1.5rem -2rem -2.5rem -1rem;
  min-height: calc(100vh - 80px);
  color: #e2e8f0;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  --tc-surface: rgba(255, 255, 255, 0.05);
  --tc-surface-hover: rgba(255, 255, 255, 0.08);
  --tc-border: rgba(255, 255, 255, 0.1);
  --tc-text: #e2e8f0;
  --tc-text-muted: rgba(255, 255, 255, 0.6);
  --tc-text-dim: rgba(255, 255, 255, 0.4);
  --tc-primary: #8b5cf6;
}

/* Page Header */
.page-header {
  padding: 1.5rem 1.5rem;
  background: var(--tc-surface);
  border-radius: var(--radius-lg);
  border: 1px solid var(--tc-border);
  margin-bottom: 1.5rem;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.title-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.title-section h1 {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
  color: var(--tc-text);
}

.subtitle {
  font-size: 0.875rem;
  color: var(--tc-text-muted);
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 0.75rem;
}

/* Cards */
.card {
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  background: var(--tc-surface);
  border: 1px solid var(--tc-border);
  border-radius: var(--radius-lg);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--tc-border);
}

.card-header h2 {
  font-size: 1.125rem;
  font-weight: 600;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--tc-text);
}

/* State Grid */
.state-grid {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.state-section {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--tc-border);
}

.state-section:last-of-type {
  border-bottom: none;
}

.state-item {
  min-width: 140px;
}

.state-item.wide {
  min-width: 280px;
}

.label {
  display: block;
  font-size: 0.7rem;
  color: var(--tc-text-dim);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.25rem;
}

.value {
  font-size: 0.95rem;
  color: var(--tc-text);
  font-weight: 500;
}

.value.mono {
  font-family: var(--font-mono);
  font-size: 0.85rem;
}

.value.small {
  font-size: 0.75rem;
  color: var(--tc-text-muted);
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.badge-success { background: rgba(16, 185, 129, 0.15); color: #10b981; }
.badge-info { background: rgba(59, 130, 246, 0.15); color: #3b82f6; }
.badge-primary { background: rgba(99, 102, 241, 0.15); color: var(--color-primary-500); }
.badge-warning { background: rgba(245, 158, 11, 0.15); color: #f59e0b; }
.badge-neutral { background: var(--tc-surface); color: var(--tc-text-muted); }

/* Flag Chips */
.flags-section {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding-top: 0.5rem;
}

.flag-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.375rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.flag-success { background: rgba(16, 185, 129, 0.12); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.25); }
.flag-error { background: rgba(239, 68, 68, 0.12); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.25); }
.flag-warning { background: rgba(245, 158, 11, 0.12); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.25); }
.flag-neutral { background: var(--tc-surface); color: var(--tc-text-dim); border: 1px solid var(--tc-border); }

/* Quote Card */
.quote-card {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1rem;
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.2);
  border-radius: 8px;
}

.quote-value {
  font-weight: 600;
  color: #10b981;
}

/* Verification Row */
.verification-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding-top: 0.5rem;
}

.verification-badges {
  display: flex;
  gap: 0.5rem;
}

.mini-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 500;
}

.mini-success { background: rgba(16, 185, 129, 0.12); color: #10b981; }
.mini-inactive { background: var(--tc-surface); color: var(--tc-text-dim); }

/* JSON Section */
.json-section {
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid var(--tc-border);
}

.json-section h3 {
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: var(--tc-text-muted);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.json-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 0.5rem;
}

.json-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 6px;
  font-size: 0.8rem;
  overflow: hidden;
}

/* Context Groups (Normalized Conversation Data) */
.context-groups {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.context-group {
  padding: 0.75rem;
  background: rgba(0, 0, 0, 0.15);
  border-radius: 8px;
}

.context-group-label {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--tc-text-dim);
  margin-bottom: 0.5rem;
}

.context-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.375rem;
}

.context-chip {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.625rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

.chip-success {
  background: rgba(16, 185, 129, 0.15);
  color: #10b981;
}

.chip-error {
  background: rgba(239, 68, 68, 0.15);
  color: #ef4444;
}

.chip-neutral {
  background: var(--tc-surface);
  color: var(--tc-text-muted);
}

.context-items {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 0.5rem;
}

.context-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  padding: 0.5rem 0.75rem;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 4px;
  font-size: 0.8rem;
  min-width: 0;
}

.context-key {
  color: var(--tc-text-dim);
  flex-shrink: 0;
  white-space: nowrap;
}

.context-key::after {
  content: ':';
  margin-right: 0.25rem;
}

.context-value {
  color: var(--tc-text);
  font-weight: 500;
  text-align: right;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 0;
  flex: 1;
}

.value-true { color: #10b981; }
.value-false { color: #ef4444; }

/* Empty State */
.empty-state {
  text-align: center;
  padding: 3rem;
  color: var(--tc-text-dim);
}

.empty-state p {
  margin-top: 1rem;
}

/* Buttons */
button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-call {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
}

.btn-call:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
}

.btn-webrtc {
  background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
  color: white;
}

.btn-webrtc:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
}

.btn-secondary {
  background: var(--tc-surface);
  color: var(--tc-text);
  border: 1px solid var(--tc-border);
}

.btn-secondary:hover:not(:disabled) {
  background: var(--tc-surface-hover);
  border-color: var(--tc-primary);
}

/* Actions Grid */
.actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1rem;
}

.action-btn {
  flex-direction: column;
  padding: 1.25rem;
  text-align: center;
  border-radius: 12px;
  background: var(--tc-surface);
  border: 1px solid var(--tc-border);
  color: var(--tc-text);
}

.action-btn span {
  font-weight: 600;
}

.action-btn small {
  font-size: 0.7rem;
  color: var(--tc-text-dim);
  font-weight: 400;
}

.action-btn:hover:not(:disabled) {
  transform: translateY(-2px);
}

.action-primary:hover:not(:disabled) { border-color: #3b82f6; background: rgba(59, 130, 246, 0.1); }
.action-success:hover:not(:disabled) { border-color: #10b981; background: rgba(16, 185, 129, 0.1); }
.action-info:hover:not(:disabled) { border-color: var(--tc-primary); background: rgba(139, 92, 246, 0.1); }
.action-warning:hover:not(:disabled) { border-color: #f59e0b; background: rgba(245, 158, 11, 0.1); }
.action-danger:hover:not(:disabled) { border-color: #ef4444; background: rgba(239, 68, 68, 0.1); }

/* Scenarios Grid */
.scenarios-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1rem;
}

.scenario-card {
  padding: 1.5rem 1rem;
  background: var(--tc-surface);
  border: 1px solid var(--tc-border);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
}

.scenario-card:hover:not(.disabled) {
  background: rgba(139, 92, 246, 0.1);
  border-color: rgba(139, 92, 246, 0.3);
  transform: translateY(-2px);
}

.scenario-card.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.scenario-icon {
  color: var(--tc-primary);
  margin-bottom: 0.75rem;
}

.scenario-title {
  font-weight: 600;
  margin-bottom: 0.25rem;
  font-size: 0.9rem;
  color: var(--tc-text);
}

.scenario-desc {
  font-size: 0.75rem;
  color: var(--tc-text-dim);
}

/* Toast */
.toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  box-shadow: var(--shadow-lg);
  z-index: 1000;
}

.toast.success {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
}

.toast.error {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  color: white;
}

.toast-enter-active, .toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from, .toast-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Responsive */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .card {
    padding: 1rem;
  }
  
  .state-section {
    gap: 1rem;
  }
}
</style>
